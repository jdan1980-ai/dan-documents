import { useMemo, useState } from 'react'
import { CHRONOTYPES } from '../data/chronotypes'
import { NEEDS } from '../data/needs'
import { ROLES } from '../data/roles'
import { dayLength, toMin } from '../lib/time'
import type { ChronotypeId, NeedId, PlanSettings, RoleId } from '../types'

const STEP_TITLES = ['Ваш ритм', 'Ваша роль', 'Приоритеты и время']

interface Props {
  initial?: PlanSettings | null
  onComplete: (settings: PlanSettings) => void
  onCancel?: () => void
}

export default function Onboarding({ initial, onComplete, onCancel }: Props) {
  const [step, setStep] = useState(0)
  const [chronotypeId, setChronotypeId] = useState<ChronotypeId>(initial?.chronotypeId ?? 'dove')
  const [roleId, setRoleId] = useState<RoleId>(initial?.roleId ?? 'remote')
  const [needIds, setNeedIds] = useState<NeedId[]>(
    initial?.needIds ?? ROLES.find((r) => r.id === (initial?.roleId ?? 'remote'))!.defaultNeeds,
  )
  const initialChronotype = CHRONOTYPES.find((c) => c.id === (initial?.chronotypeId ?? 'dove'))!
  const [wake, setWake] = useState(initial?.wake ?? initialChronotype.defaultWake)
  const [sleep, setSleep] = useState(initial?.sleep ?? initialChronotype.defaultSleep)
  const [timesTouched, setTimesTouched] = useState(Boolean(initial))

  const role = useMemo(() => ROLES.find((r) => r.id === roleId)!, [roleId])

  const awakeMinutes = wake && sleep ? dayLength(toMin(wake), toMin(sleep)) : 0
  const awakeHours = (awakeMinutes / 60).toFixed(1)
  const timeWarning = awakeMinutes > 0 && (awakeMinutes < 4 * 60 || awakeMinutes > 20 * 60)

  function toggleNeed(id: NeedId) {
    setNeedIds((prev) => (prev.includes(id) ? prev.filter((n) => n !== id) : [...prev, id]))
  }

  function resetNeeds() {
    setNeedIds(role.defaultNeeds)
  }

  function handleFinish() {
    onComplete({ chronotypeId, roleId, needIds, wake, sleep })
  }

  return (
    <div className="mx-auto flex w-full max-w-3xl flex-col gap-6 px-4 py-10">
      <header className="text-center">
        <h1 className="text-2xl font-semibold text-slate-900 sm:text-3xl">Соберём ваш идеальный день</h1>
        <p className="mt-2 text-slate-500">
          Три коротких шага — и вы получите расписание, подстроенное под ваш ритм и задачи.
        </p>
      </header>

      <ol className="flex items-center justify-center gap-2 text-sm">
        {STEP_TITLES.map((title, i) => (
          <li key={title} className="flex items-center gap-2">
            <span
              className={`flex h-7 w-7 items-center justify-center rounded-full font-medium ${
                i === step
                  ? 'bg-violet-600 text-white'
                  : i < step
                    ? 'bg-violet-100 text-violet-700'
                    : 'bg-slate-100 text-slate-400'
              }`}
            >
              {i + 1}
            </span>
            <span className={i === step ? 'text-slate-900' : 'text-slate-400'}>{title}</span>
            {i < STEP_TITLES.length - 1 && <span className="mx-1 h-px w-6 bg-slate-200" />}
          </li>
        ))}
      </ol>

      {step === 0 && (
        <div className="grid gap-3 sm:grid-cols-3">
          {CHRONOTYPES.map((c) => (
            <button
              key={c.id}
              type="button"
              onClick={() => {
                setChronotypeId(c.id)
                if (!timesTouched) {
                  setWake(c.defaultWake)
                  setSleep(c.defaultSleep)
                }
              }}
              className={`flex flex-col gap-2 rounded-2xl border p-4 text-left transition ${
                chronotypeId === c.id
                  ? 'border-violet-500 bg-violet-50 ring-2 ring-violet-200'
                  : 'border-slate-200 bg-white hover:border-violet-300'
              }`}
            >
              <span className="text-3xl">{c.emoji}</span>
              <span className="font-semibold text-slate-900">{c.label}</span>
              <span className="text-sm font-medium text-violet-700">{c.tagline}</span>
              <span className="text-sm text-slate-500">{c.description}</span>
            </button>
          ))}
        </div>
      )}

      {step === 1 && (
        <div className="grid gap-3 sm:grid-cols-2">
          {ROLES.map((r) => (
            <button
              key={r.id}
              type="button"
              onClick={() => {
                setRoleId(r.id)
                setNeedIds(r.defaultNeeds)
              }}
              className={`flex flex-col gap-1 rounded-2xl border p-4 text-left transition ${
                roleId === r.id
                  ? 'border-violet-500 bg-violet-50 ring-2 ring-violet-200'
                  : 'border-slate-200 bg-white hover:border-violet-300'
              }`}
            >
              <span className="text-2xl">{r.emoji}</span>
              <span className="font-semibold text-slate-900">{r.label}</span>
              <span className="text-sm text-slate-500">{r.description}</span>
            </button>
          ))}
        </div>
      )}

      {step === 2 && (
        <div className="flex flex-col gap-6">
          <div>
            <div className="mb-2 flex items-center justify-between">
              <h2 className="font-semibold text-slate-900">Что для вас важно сегодня?</h2>
              <button type="button" onClick={resetNeeds} className="text-sm text-violet-600 hover:underline">
                Сбросить к рекомендованным
              </button>
            </div>
            <p className="mb-3 text-sm text-slate-500">
              Выберите пункты в порядке важности — первым нажимайте самый приоритетный. Мы выделим на него больше
              времени и лучший момент по энергии.
            </p>
            <div className="flex flex-wrap gap-2">
              {NEEDS.map((n) => {
                const idx = needIds.indexOf(n.id)
                const active = idx !== -1
                return (
                  <button
                    key={n.id}
                    type="button"
                    onClick={() => toggleNeed(n.id)}
                    className={`flex items-center gap-1.5 rounded-full border px-3 py-1.5 text-sm transition ${
                      active
                        ? 'border-violet-500 bg-violet-600 text-white'
                        : 'border-slate-200 bg-white text-slate-700 hover:border-violet-300'
                    }`}
                  >
                    {active && <span className="grid h-4 w-4 place-items-center rounded-full bg-white/25 text-[11px]">{idx + 1}</span>}
                    <span>{n.emoji}</span>
                    <span>{n.label}</span>
                  </button>
                )
              })}
            </div>
          </div>

          <div className="grid gap-4 sm:grid-cols-2">
            <label className="flex flex-col gap-1 text-sm font-medium text-slate-700">
              Подъём
              <input
                type="time"
                value={wake}
                onChange={(e) => {
                  setTimesTouched(true)
                  setWake(e.target.value)
                }}
                className="rounded-xl border border-slate-200 px-3 py-2 text-base text-slate-900 focus:border-violet-500 focus:outline-none"
              />
            </label>
            <label className="flex flex-col gap-1 text-sm font-medium text-slate-700">
              Отбой
              <input
                type="time"
                value={sleep}
                onChange={(e) => {
                  setTimesTouched(true)
                  setSleep(e.target.value)
                }}
                className="rounded-xl border border-slate-200 px-3 py-2 text-base text-slate-900 focus:border-violet-500 focus:outline-none"
              />
            </label>
          </div>
          <p className={`text-sm ${timeWarning ? 'text-amber-600' : 'text-slate-400'}`}>
            Время бодрствования: ~{awakeHours} ч.{' '}
            {timeWarning && 'Проверьте время — расписание может получиться странным.'}
          </p>
        </div>
      )}

      <div className="mt-2 flex items-center justify-between">
        <button
          type="button"
          onClick={() => (step === 0 ? onCancel?.() : setStep((s) => s - 1))}
          className="rounded-xl px-4 py-2 text-slate-500 hover:text-slate-800"
        >
          {step === 0 ? (onCancel ? 'Отмена' : '') : '← Назад'}
        </button>
        {step < 2 ? (
          <button
            type="button"
            onClick={() => setStep((s) => s + 1)}
            className="rounded-xl bg-violet-600 px-6 py-2.5 font-medium text-white shadow-sm transition hover:bg-violet-700"
          >
            Далее →
          </button>
        ) : (
          <button
            type="button"
            disabled={needIds.length === 0 || !wake || !sleep}
            onClick={handleFinish}
            className="rounded-xl bg-violet-600 px-6 py-2.5 font-medium text-white shadow-sm transition hover:bg-violet-700 disabled:cursor-not-allowed disabled:bg-slate-300"
          >
            Построить день ✨
          </button>
        )}
      </div>
    </div>
  )
}
