import { useEffect, useState } from 'react'
import { formatClock, formatDuration, relativeFromClock, toMin } from '../lib/time'
import type { PlanBlock } from '../types'

interface Props {
  blocks: PlanBlock[]
  wakeMin: number
  done: Record<string, boolean>
  onToggleDone: (id: string) => void
  onUpdateTime: (id: string, startRel: number, endRel: number) => void
  onDelete: (id: string) => void
}

const KIND_LABEL: Record<PlanBlock['kind'], string> = {
  routine: 'Рутина',
  meal: 'Приём пищи',
  commitment: 'Обязательное',
  need: 'Приоритет',
  buffer: 'Свободно',
  custom: 'Своя задача',
}

export default function Timeline({ blocks, wakeMin, done, onToggleDone, onUpdateTime, onDelete }: Props) {
  const [nowRel, setNowRel] = useState(() => currentRel(wakeMin))
  const [editingId, setEditingId] = useState<string | null>(null)

  useEffect(() => {
    const id = setInterval(() => setNowRel(currentRel(wakeMin)), 60_000)
    return () => clearInterval(id)
  }, [wakeMin])

  return (
    <ol className="relative flex flex-col gap-0 border-l-2 border-slate-100 pl-0">
      {blocks.map((b) => {
        const isCurrent = nowRel >= b.startRel && nowRel < b.endRel
        const isDone = Boolean(done[b.id])
        const isEditing = editingId === b.id
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
                <div className="min-w-0 flex-1">
                  <div className="flex flex-wrap items-baseline gap-x-2 gap-y-0.5">
                    <span className={`font-medium text-slate-900 ${isDone ? 'line-through' : ''}`}>{b.label}</span>
                    {isCurrent && (
                      <span className="rounded-full bg-violet-600 px-2 py-0.5 text-[11px] font-semibold text-white">
                        сейчас
                      </span>
                    )}
                  </div>

                  {isEditing ? (
                    <TimeEditor
                      wakeMin={wakeMin}
                      startRel={b.startRel}
                      endRel={b.endRel}
                      onCancel={() => setEditingId(null)}
                      onSave={(startRel, endRel) => {
                        onUpdateTime(b.id, startRel, endRel)
                        setEditingId(null)
                      }}
                    />
                  ) : (
                    <div className="mt-0.5 flex flex-wrap items-center gap-x-2 gap-y-1 text-sm text-slate-500">
                      <span>
                        {formatClock(wakeMin + b.startRel)}–{formatClock(wakeMin + b.endRel)} ·{' '}
                        {formatDuration(b.endRel - b.startRel)} · {KIND_LABEL[b.kind]}
                      </span>
                      <button
                        type="button"
                        onClick={() => setEditingId(b.id)}
                        className="text-violet-600 hover:underline"
                      >
                        изменить время
                      </button>
                    </div>
                  )}
                </div>
              </div>
              <div className="flex shrink-0 items-center gap-2 pt-0.5">
                <label className="flex cursor-pointer items-center">
                  <input
                    type="checkbox"
                    checked={isDone}
                    onChange={() => onToggleDone(b.id)}
                    className="h-5 w-5 rounded border-slate-300 text-violet-600 focus:ring-violet-500"
                  />
                </label>
                <button
                  type="button"
                  onClick={() => onDelete(b.id)}
                  aria-label="Удалить блок"
                  className="text-slate-300 hover:text-red-500"
                >
                  ✕
                </button>
              </div>
            </div>
          </li>
        )
      })}
    </ol>
  )
}

function TimeEditor({
  wakeMin,
  startRel,
  endRel,
  onSave,
  onCancel,
}: {
  wakeMin: number
  startRel: number
  endRel: number
  onSave: (startRel: number, endRel: number) => void
  onCancel: () => void
}) {
  const [start, setStart] = useState(formatClock(wakeMin + startRel))
  const [end, setEnd] = useState(formatClock(wakeMin + endRel))
  const invalid = !start || !end

  function handleSave() {
    const startClock = toMin(start)
    const endClock = toMin(end)
    const newStartRel = relativeFromClock(startClock, wakeMin)
    let newEndRel = relativeFromClock(endClock, wakeMin)
    if (newEndRel <= newStartRel) newEndRel += 1440
    onSave(newStartRel, newEndRel)
  }

  return (
    <div className="mt-1.5 flex flex-wrap items-center gap-2 text-sm">
      <input
        type="time"
        value={start}
        onChange={(e) => setStart(e.target.value)}
        className="rounded-lg border border-slate-200 px-2 py-1 text-slate-900 focus:border-violet-500 focus:outline-none"
      />
      <span className="text-slate-400">–</span>
      <input
        type="time"
        value={end}
        onChange={(e) => setEnd(e.target.value)}
        className="rounded-lg border border-slate-200 px-2 py-1 text-slate-900 focus:border-violet-500 focus:outline-none"
      />
      <button
        type="button"
        disabled={invalid}
        onClick={handleSave}
        className="rounded-lg bg-violet-600 px-2.5 py-1 font-medium text-white hover:bg-violet-700 disabled:bg-slate-300"
      >
        Сохранить
      </button>
      <button type="button" onClick={onCancel} className="text-slate-400 hover:text-slate-700">
        Отмена
      </button>
    </div>
  )
}

function currentRel(wakeMin: number): number {
  const now = new Date()
  return relativeFromClock(now.getHours() * 60 + now.getMinutes(), wakeMin)
}
