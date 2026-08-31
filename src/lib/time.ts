export function toMin(hhmm: string): number {
  const [h, m] = hhmm.split(':').map(Number)
  return h * 60 + m
}

export function formatClock(min: number): string {
  const wrapped = ((min % 1440) + 1440) % 1440
  const h = Math.floor(wrapped / 60)
  const m = Math.round(wrapped % 60)
  return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}`
}

export function formatDuration(min: number): string {
  const h = Math.floor(min / 60)
  const m = Math.round(min % 60)
  if (h === 0) return `${m} мин`
  if (m === 0) return `${h} ч`
  return `${h} ч ${m} мин`
}

/** minutes from wake (0) to given absolute clock time, always positive, wraps past midnight */
export function relativeFromClock(clockMin: number, wakeMin: number): number {
  return ((clockMin - wakeMin) % 1440 + 1440) % 1440
}

/** length of the waking day in minutes, always positive */
export function dayLength(wakeMin: number, sleepMin: number): number {
  const len = ((sleepMin - wakeMin) % 1440 + 1440) % 1440
  return len === 0 ? 1440 : len
}
