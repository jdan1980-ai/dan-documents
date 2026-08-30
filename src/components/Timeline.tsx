import { useEffect, useState } from 'react'
import { formatClock, formatDuration, relativeFromClock } from '../lib/time'
import type { PlanBlock } from '../types'

interface Props {
  blocks: PlanBlock[]
  wakeMin: number
  done: Record<string, boolean>
  onToggleDone: (id: string) => void
}

const KIND_LABEL: Record<PlanBlock['kind'], string> = {
  routine: 'Рутина',
  meal: 'Приём пищи',
  commitment: 'Обязательное',
  need: 'Приоритет',
  buffer: 'Свободно',
}

export default function Timeline({ blocks, wakeMin, done, onToggleDone }: Props) {
  const [nowRel, setNowRel] = useState(() => currentRel(wakeMin))

  useEffect(() => {
    const id = setInterval(() => setNowRel(currentRel(wakeMin)), 60_000)
    return () => clearInterval(id)
  }, [wakeMin])

  return (
    <ol className="relative flex flex-col gap-0 border-l-2 border-slate-100 pl-0">
      {blocks.map((b) => {
        const isCurrent = nowRel >= b.startRel && nowRel < b.endRel
        const isDone = Boolean(done[b.id])
        return (
          <li key={b.id} className="relative flex gap-4 pb-5 pl-6">
            <span
              className="absolute left-[-7px] top-1.5 h-3 w-3 rounded-full border-2 border-white shadow"
              style={{ background: b.color }}
              aria-hidden
            />
            <div
              className={`flex w-full items-start justify-between gap-3 rounded-2xl border p-3.5 transition ${
                isCurrent ? 'border-violet-400 bg-violet-50 shadow-sm' : 'border-slate-100 bg-white'
              } ${isDone ? 'opacity-50' : ''}`}
            >
              <div className="flex min-w-0 flex-1 items-start gap-3">
                <span className="text-xl leading-none">{b.emoji}</span>
                <div className="min-w-0">
                  <div className="flex flex-wrap items-baseline gap-x-2 gap-y-0.5">
                    <span className={`font-medium text-slate-900 ${isDone ? 'line-through' : ''}`}>{b.label}</span>
                    {isCurrent && (
                      <span className="rounded-full bg-violet-600 px-2 py-0.5 text-[11px] font-semibold text-white">
                        сейчас
                      </span>
                    )}
                  </div>
                  <div className="mt-0.5 text-sm text-slate-500">
                    {formatClock(wakeMin + b.startRel)}–{formatClock(wakeMin + b.endRel)} ·{' '}
                    {formatDuration(b.endRel - b.startRel)} · {KIND_LABEL[b.kind]}
                  </div>
                </div>
              </div>
              <label className="flex shrink-0 cursor-pointer items-center pt-0.5">
                <input
                  type="checkbox"
                  checked={isDone}
                  onChange={() => onToggleDone(b.id)}
                  className="h-5 w-5 rounded border-slate-300 text-violet-600 focus:ring-violet-500"
                />
              </label>
            </div>
          </li>
        )
      })}
    </ol>
  )
}

function currentRel(wakeMin: number): number {
  const now = new Date()
  return relativeFromClock(now.getHours() * 60 + now.getMinutes(), wakeMin)
}
