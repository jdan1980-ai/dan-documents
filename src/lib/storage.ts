import type { PlanSettings } from '../types'

const SETTINGS_KEY = 'day-planner:settings'
const DONE_KEY = 'day-planner:done'

export function loadSettings(): PlanSettings | null {
  try {
    const raw = localStorage.getItem(SETTINGS_KEY)
    return raw ? (JSON.parse(raw) as PlanSettings) : null
  } catch {
    return null
  }
}

export function saveSettings(settings: PlanSettings) {
  try {
    localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings))
  } catch {
    // ignore quota / privacy-mode errors
  }
}

export function clearSettings() {
  try {
    localStorage.removeItem(SETTINGS_KEY)
    localStorage.removeItem(DONE_KEY)
  } catch {
    // ignore
  }
}

export function loadDone(): Record<string, boolean> {
  try {
    const raw = localStorage.getItem(DONE_KEY)
    return raw ? (JSON.parse(raw) as Record<string, boolean>) : {}
  } catch {
    return {}
  }
}

export function saveDone(done: Record<string, boolean>) {
  try {
    localStorage.setItem(DONE_KEY, JSON.stringify(done))
  } catch {
    // ignore
  }
}
