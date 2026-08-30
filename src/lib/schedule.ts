import type { Chronotype, EnergyLevel, Need, PlanBlock, Role } from '../types'
import { dayLength, relativeFromClock, toMin } from './time'

interface SkeletonItem {
  label: string
  emoji: string
  startRel: number
  endRel: number
  kind: PlanBlock['kind']
  color: string
  splitForLunch?: boolean
}

const ROUTINE_COLOR = '#94a3b8'
const MEAL_COLOR = '#f59e0b'
const COMMITMENT_COLOR = '#334155'
const BUFFER_COLOR = '#cbd5e1'

let idCounter = 0
function nextId() {
  idCounter += 1
  return `blk-${idCounter}`
}

export function generateSchedule(
  chronotype: Chronotype,
  role: Role,
  needs: Need[],
  wake: string,
  sleep: string,
): PlanBlock[] {
  const wakeMin = toMin(wake)
  const total = dayLength(wakeMin, toMin(sleep))

  const skeleton: SkeletonItem[] = [
    {
      label: 'Подъём, водные процедуры',
      emoji: '🪥',
      startRel: 0,
      endRel: Math.min(30, total),
      kind: 'routine',
      color: ROUTINE_COLOR,
    },
    {
      label: 'Завтрак',
      emoji: '🍳',
      startRel: 30,
      endRel: 55,
      kind: 'meal',
      color: MEAL_COLOR,
    },
  ]

  for (const fb of role.fixedBlocks) {
    const startRel =
      fb.anchor === 'clock'
        ? relativeFromClock(toMin(fb.start as string), wakeMin)
        : (fb.start as number)
    skeleton.push({
      label: fb.label,
      emoji: fb.emoji,
      startRel,
      endRel: startRel + fb.durationMin,
      kind: 'commitment',
      color: COMMITMENT_COLOR,
      splitForLunch: fb.splitForLunch,
    })
  }

  skeleton.sort((a, b) => a.startRel - b.startRel)
  resolveOverlaps(skeleton)

  let fixed = skeleton
    .map((b) => ({ ...b, endRel: Math.min(b.endRel, total) }))
    .filter((b) => b.startRel < total && b.endRel - b.startRel >= 10)

  fixed = insertMeal(
    fixed,
    { label: 'Обед', emoji: '🍲', targetRel: relativeFromClock(13 * 60, wakeMin), durationMin: 40 },
    total,
  )
  fixed = insertMeal(
    fixed,
    { label: 'Ужин', emoji: '🍽️', targetRel: relativeFromClock(19 * 60 + 30, wakeMin), durationMin: 40 },
    total,
  )

  const windDownStart = Math.max(0, total - 40)
  if (!fixed.some((i) => i.startRel < total && i.endRel > windDownStart)) {
    fixed.push({
      label: 'Подготовка ко сну',
      emoji: '🌌',
      startRel: windDownStart,
      endRel: total,
      kind: 'routine',
      color: ROUTINE_COLOR,
    })
  }

  fixed.sort((a, b) => a.startRel - b.startRel)

  const gaps: { start: number; end: number }[] = []
  let cursor = 0
  for (const b of fixed) {
    if (b.startRel > cursor) gaps.push({ start: cursor, end: b.startRel })
    cursor = Math.max(cursor, b.endRel)
  }
  if (cursor < total) gaps.push({ start: cursor, end: total })

  function energyAt(rel: number): EnergyLevel {
    const clock = ((wakeMin + rel) % 1440 + 1440) % 1440
    const win = chronotype.energy.find((w) => clock >= w.startMin && clock < w.endMin)
    return win?.level ?? 'medium'
  }

  const gapInfos = gaps
    .filter((g) => g.end - g.start >= 15)
    .map((g) => ({ start: g.start, end: g.end, remaining: g.end - g.start, level: energyAt((g.start + g.end) / 2) }))

  const needBlocks: SkeletonItem[] = []

  function weightOf(n: Need) {
    // needs are ordered by user-chosen priority; earlier picks get proportionally more time
    const idx = needs.indexOf(n)
    const priorityBoost = 1 + (needs.length - 1 - idx) * 0.5
    return n.weight * (role.weightOverrides?.[n.id] ?? 1) * priorityBoost
  }

  const sumWeights = needs.reduce((s, n) => s + weightOf(n), 0)
  const totalFree = gapInfos.reduce((s, g) => s + g.remaining, 0)

  const targets = new Map<string, number>()
  for (const n of needs) {
    const raw = sumWeights > 0 ? (totalFree * weightOf(n)) / sumWeights : 0
    targets.set(n.id, clamp(raw, n.minSession, n.maxSession * 2))
  }

  function placeInBestGap(need: Need, amount: number): number {
    let candidates = gapInfos.filter((g) => g.level === need.idealEnergy && g.remaining >= need.minSession)
    if (candidates.length === 0) candidates = gapInfos.filter((g) => g.remaining >= need.minSession)
    if (candidates.length === 0) return 0
    candidates.sort((a, b) => b.remaining - a.remaining)
    const gap = candidates[0]
    const session = Math.min(amount, gap.remaining, need.maxSession)
    if (session < need.minSession) return 0
    needBlocks.push({
      label: need.label,
      emoji: need.emoji,
      startRel: gap.start,
      endRel: gap.start + session,
      kind: 'need',
      color: need.color,
    })
    gap.start += session
    gap.remaining -= session
    return session
  }

  const placed = new Map<string, number>()
  for (const n of needs) {
    const amount = targets.get(n.id) ?? n.minSession
    placed.set(n.id, placeInBestGap(n, Math.min(Math.max(amount, n.minSession), n.maxSession)))
  }

  for (let round = 0; round < 3; round++) {
    let any = false
    for (const n of needs) {
      const target = targets.get(n.id) ?? 0
      const already = placed.get(n.id) ?? 0
      if (already >= target) continue
      const got = placeInBestGap(n, Math.min(target - already, n.maxSession))
      if (got > 0) {
        placed.set(n.id, already + got)
        any = true
      }
    }
    if (!any) break
  }

  for (const g of gapInfos) {
    if (g.remaining >= 15) {
      needBlocks.push({
        label: 'Личное время',
        emoji: '⏳',
        startRel: g.start,
        endRel: g.start + g.remaining,
        kind: 'buffer',
        color: BUFFER_COLOR,
      })
    }
  }

  const all = [...fixed, ...needBlocks].sort((a, b) => a.startRel - b.startRel)

  return all.map((b) => ({
    id: nextId(),
    label: b.label,
    emoji: b.emoji,
    startRel: Math.round(b.startRel),
    endRel: Math.round(b.endRel),
    kind: b.kind,
    color: b.color,
  }))
}

function clamp(v: number, min: number, max: number) {
  return Math.max(min, Math.min(max, v))
}

function resolveOverlaps(items: SkeletonItem[]) {
  for (let i = 1; i < items.length; i++) {
    const prev = items[i - 1]
    const cur = items[i]
    if (cur.startRel < prev.endRel) {
      const shift = prev.endRel - cur.startRel
      cur.startRel += shift
      cur.endRel += shift
    }
  }
}

function insertMeal(
  items: SkeletonItem[],
  meal: { label: string; emoji: string; targetRel: number; durationMin: number },
  total: number,
) {
  if (meal.targetRel >= total) return items

  const hitIdx = items.findIndex(
    (i) => i.splitForLunch && meal.targetRel > i.startRel + 10 && meal.targetRel < i.endRel - 10,
  )
  if (hitIdx !== -1) {
    const hit = items[hitIdx]
    const before: SkeletonItem = { ...hit, endRel: meal.targetRel }
    const after: SkeletonItem = { ...hit, startRel: meal.targetRel + meal.durationMin }
    const mealBlock: SkeletonItem = {
      label: meal.label,
      emoji: meal.emoji,
      startRel: meal.targetRel,
      endRel: meal.targetRel + meal.durationMin,
      kind: 'meal',
      color: MEAL_COLOR,
    }
    const result = [...items]
    result.splice(hitIdx, 1, before, mealBlock, after)
    return result.filter((b) => b.endRel - b.startRel >= 5)
  }

  const overlapping = items.find(
    (i) => i.startRel < meal.targetRel + meal.durationMin && i.endRel > meal.targetRel,
  )
  let start = meal.targetRel
  if (overlapping) start = overlapping.endRel
  let end = start + meal.durationMin
  if (end > total) {
    end = total
    start = Math.max(0, end - meal.durationMin)
  }
  if (end - start < 10) return items

  const result = [
    ...items,
    { label: meal.label, emoji: meal.emoji, startRel: start, endRel: end, kind: 'meal' as const, color: MEAL_COLOR },
  ]
  result.sort((a, b) => a.startRel - b.startRel)
  resolveOverlaps(result)
  return result
    .filter((b) => b.startRel < total && b.endRel - b.startRel >= 5)
    .map((b) => ({ ...b, endRel: Math.min(b.endRel, total) }))
}
