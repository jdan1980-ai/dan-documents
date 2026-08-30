export type ChronotypeId = 'lark' | 'dove' | 'owl'

export type EnergyLevel = 'high' | 'medium' | 'low'

export interface EnergyWindow {
  /** absolute clock minutes, 0–1440, non-wrapping */
  startMin: number
  endMin: number
  level: EnergyLevel
}

export interface Chronotype {
  id: ChronotypeId
  label: string
  emoji: string
  tagline: string
  description: string
  defaultWake: string
  defaultSleep: string
  energy: EnergyWindow[]
}

export type NeedId =
  | 'deep_work'
  | 'study'
  | 'sport'
  | 'family'
  | 'creativity'
  | 'rest'
  | 'social'
  | 'chores'
  | 'learning'

export interface Need {
  id: NeedId
  label: string
  emoji: string
  idealEnergy: EnergyLevel
  weight: number
  minSession: number
  maxSession: number
  color: string
}

export type RoleId =
  | 'student'
  | 'office'
  | 'remote'
  | 'freelancer'
  | 'parent'
  | 'entrepreneur'
  | 'athlete'

export interface FixedBlockTemplate {
  label: string
  emoji: string
  anchor: 'clock' | 'afterWake'
  /** 'HH:MM' when anchor is 'clock', minutes offset from wake when 'afterWake' */
  start: string | number
  durationMin: number
  splitForLunch?: boolean
}

export interface Role {
  id: RoleId
  label: string
  emoji: string
  description: string
  fixedBlocks: FixedBlockTemplate[]
  defaultNeeds: NeedId[]
  weightOverrides?: Partial<Record<NeedId, number>>
}

export type BlockKind = 'routine' | 'meal' | 'commitment' | 'need' | 'buffer'

export interface PlanBlock {
  id: string
  label: string
  emoji: string
  /** minutes relative to wake time, 0 = wake moment */
  startRel: number
  endRel: number
  kind: BlockKind
  color: string
}

export interface PlanSettings {
  chronotypeId: ChronotypeId
  roleId: RoleId
  needIds: NeedId[]
  wake: string
  sleep: string
}
