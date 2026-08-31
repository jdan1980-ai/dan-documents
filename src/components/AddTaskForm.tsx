import { useState } from 'react'
import { formatClock, relativeFromClock, toMin } from '../lib/time'
import type { PlanBlock } from '../types'

interface Props {
  wakeMin: number
  blocks: PlanBlock[]
  onAdd: (label: string, emoji: string, startRel: number, endRel: number) => void
}

const EMOJI_OPTIONS = ['📝', '📌', '☎️', '🛒', '💊', '🐕', '🚗', '✉️']

export default function AddTaskForm({ wakeMin, blocks, onAdd }: Props) {
  const lastEnd = blocks.length > 0 ? Math.max(...blocks.map((b) => b.endRel)) : 0
  const [open, setOpen] = useState(false)
  const [label, setLabel] = useState('')
  const [emoji, setEmoji] = useState(EMOJI_OPTIONS[0])
  const [start, setStart] = useState(formatClock(wakeMin + lastEnd))
  const [end, setEnd] = useState(formatClock(wakeMin + lastEnd + 30))

  const trimmed = label.trim()
  const canSubmit = trimmed.length > 0 && start && end

  function reset() {
    setLabel('')
    setEmoji(EMOJI_OPTIONS[0])
    setStart(formatClock(wakeMin + lastEnd))
    setEnd(formatClock(wakeMin + lastEnd + 30))
  }

  function handleSubmit() {
    if (!canSubmit) return
    const startRel = relativeFromClock(toMin(start), wakeMin)
    let endRel = relativeFromClock(toMin(end), wakeMin)
    if (endRel <= startRel) endRel += 1440
    onAdd(trimmed, emoji, startRel, endRel)
    reset()
    setOpen(false)
  }

  if (!open) {
    return (
      <button
        type="button"
        onClick={() => setOpen(true)}
        className="mt-1 flex items-center justify-center gap-2 rounded-2xl border border-dashed border-slate-300 py-3 text-sm font-medium text-slate-500 hover:border-violet-400 hover:text-violet-600"
      >
        + Добавить свою задачу
      </button>
    )
  }

  return (
    <div className="mt-1 flex flex-col gap-3 rounded-2xl border border-violet-200 bg-white p-4">
      <div className="flex items-center gap-2">
        <select
          value={emoji}
          onChange={(e) => setEmoji(e.target.value)}
          className="rounded-lg border border-slate-200 px-2 py-2 text-lg"
          aria-label="Иконка задачи"
        >
          {EMOJI_OPTIONS.map((e) => (
            <option key={e} value={e}>
              {e}
            </option>
          ))}
        </select>
        <input
          type="text"
          value={label}
          onChange={(e) => setLabel(e.target.value)}
          placeholder="Например: позвонить в банк"
          className="flex-1 rounded-lg border border-slate-200 px-3 py-2 text-slate-900 focus:border-violet-500 focus:outline-none"
          autoFocus
        />
      </div>
      <div className="flex flex-wrap items-center gap-2 text-sm">
        <input
          type="time"
          value={start}
          onChange={(e) => setStart(e.target.value)}
          className="rounded-lg border border-slate-200 px-2 py-1.5 text-slate-900 focus:border-violet-500 focus:outline-none"
        />
        <span className="text-slate-400">–</span>
        <input
          type="time"
          value={end}
          onChange={(e) => setEnd(e.target.value)}
          className="rounded-lg border border-slate-200 px-2 py-1.5 text-slate-900 focus:border-violet-500 focus:outline-none"
        />
      </div>
      <div className="flex gap-2">
        <button
          type="button"
          disabled={!canSubmit}
          onClick={handleSubmit}
          className="rounded-xl bg-violet-600 px-4 py-2 text-sm font-medium text-white hover:bg-violet-700 disabled:cursor-not-allowed disabled:bg-slate-300"
        >
          Добавить
        </button>
        <button
          type="button"
          onClick={() => {
            reset()
            setOpen(false)
          }}
          className="rounded-xl px-4 py-2 text-sm font-medium text-slate-500 hover:text-slate-800"
        >
          Отмена
        </button>
      </div>
    </div>
  )
}
