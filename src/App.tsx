import { useMemo, useState } from 'react'
import Onboarding from './components/Onboarding'
import Timeline from './components/Timeline'
import { getChronotype } from './data/chronotypes'
import { getNeed } from './data/needs'
import { getRole } from './data/roles'
import { generateSchedule } from './lib/schedule'
import { clearSettings, loadDone, loadSettings, saveDone, saveSettings } from './lib/storage'
import { toMin } from './lib/time'
import type { PlanBlock, PlanSettings } from './types'

type View = 'onboarding' | 'plan'

export default function App() {
  const [settings, setSettings] = useState<PlanSettings | null>(() => loadSettings())
  const [view, setView] = useState<View>(() => (loadSettings() ? 'plan' : 'onboarding'))
  const [blocks, setBlocks] = useState<PlanBlock[]>(() => (settings ? buildPlan(settings) : []))
  const [done, setDone] = useState<Record<string, boolean>>(() => loadDone())

  const chronotype = settings ? getChronotype(settings.chronotypeId) : null
  const role = settings ? getRole(settings.roleId) : null

  const priorityChips = useMemo(
    () => settings?.needIds.map((id) => getNeed(id)) ?? [],
    [settings],
  )

  function handleOnboardingComplete(next: PlanSettings) {
    setSettings(next)
    saveSettings(next)
    setBlocks(buildPlan(next))
    setDone({})
    saveDone({})
    setView('plan')
  }

  function regenerate() {
    if (!settings) return
    setBlocks(buildPlan(settings))
    setDone({})
    saveDone({})
  }

  function toggleDone(id: string) {
    setDone((prev) => {
      const next = { ...prev, [id]: !prev[id] }
      saveDone(next)
      return next
    })
  }

  function startOver() {
    clearSettings()
    setSettings(null)
    setBlocks([])
    setDone({})
    setView('onboarding')
  }

  if (view === 'onboarding' || !settings || !chronotype || !role) {
    return (
      <div className="min-h-full bg-gradient-to-b from-violet-50 via-white to-white">
        <Onboarding
          initial={settings}
          onComplete={handleOnboardingComplete}
          onCancel={settings ? () => setView('plan') : undefined}
        />
      </div>
    )
  }

  const wakeMin = toMin(settings.wake)
  const doneCount = blocks.filter((b) => done[b.id]).length

  return (
    <div className="min-h-full bg-gradient-to-b from-violet-50 via-white to-white pb-16 print:bg-white">
      <div className="mx-auto flex w-full max-w-2xl flex-col gap-6 px-4 py-8">
        <header className="flex flex-col gap-4 rounded-3xl border border-violet-100 bg-white p-5 shadow-sm print:border-none print:shadow-none">
          <div className="flex items-start justify-between gap-3">
            <div>
              <p className="text-sm font-medium text-violet-600">
                {chronotype.emoji} {chronotype.label} · {role.emoji} {role.label}
              </p>
              <h1 className="text-xl font-semibold text-slate-900 sm:text-2xl">Ваш план на день</h1>
              <p className="mt-1 text-sm text-slate-500">
                {settings.wake}–{settings.sleep} · выполнено {doneCount} из {blocks.length}
              </p>
            </div>
            <div className="hidden shrink-0 text-3xl sm:block">{chronotype.emoji}</div>
          </div>
          <div className="flex flex-wrap gap-1.5">
            {priorityChips.map((n, i) => (
              <span
                key={n.id}
                className="flex items-center gap-1 rounded-full bg-slate-100 px-2.5 py-1 text-xs font-medium text-slate-600"
              >
                <span className="text-slate-400">#{i + 1}</span>
                {n.emoji} {n.label}
              </span>
            ))}
          </div>
          <div className="flex flex-wrap gap-2 print:hidden">
            <button
              type="button"
              onClick={regenerate}
              className="rounded-xl bg-violet-600 px-3.5 py-2 text-sm font-medium text-white hover:bg-violet-700"
            >
              ↻ Сгенерировать заново
            </button>
            <button
              type="button"
              onClick={() => setView('onboarding')}
              className="rounded-xl border border-slate-200 px-3.5 py-2 text-sm font-medium text-slate-700 hover:border-violet-300"
            >
              Изменить настройки
            </button>
            <button
              type="button"
              onClick={() => window.print()}
              className="rounded-xl border border-slate-200 px-3.5 py-2 text-sm font-medium text-slate-700 hover:border-violet-300"
            >
              Распечатать
            </button>
            <button
              type="button"
              onClick={startOver}
              className="ml-auto rounded-xl px-3.5 py-2 text-sm font-medium text-slate-400 hover:text-red-600"
            >
              Начать с нуля
            </button>
          </div>
        </header>

        <Timeline blocks={blocks} wakeMin={wakeMin} done={done} onToggleDone={toggleDone} />
      </div>
    </div>
  )
}

function buildPlan(settings: PlanSettings): PlanBlock[] {
  const chronotype = getChronotype(settings.chronotypeId)
  const role = getRole(settings.roleId)
  const needs = settings.needIds.map((id) => getNeed(id))
  return generateSchedule(chronotype, role, needs, settings.wake, settings.sleep)
}
