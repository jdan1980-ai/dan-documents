import type { Role } from '../types'

export const ROLES: Role[] = [
  {
    id: 'student',
    label: 'Студент / школьник',
    emoji: '🎓',
    description: 'Пары или уроки занимают основную часть дня, важно вписать учёбу, отдых и общение.',
    fixedBlocks: [
      {
        label: 'Учёба / пары',
        emoji: '🏫',
        anchor: 'clock',
        start: '09:00',
        durationMin: 5 * 60,
        splitForLunch: true,
      },
    ],
    defaultNeeds: ['study', 'social', 'rest', 'sport'],
  },
  {
    id: 'office',
    label: 'Офисный сотрудник',
    emoji: '🏢',
    description: 'Рабочий день с 9 до 18 в основном фиксирован — планируем всё вокруг него.',
    fixedBlocks: [
      {
        label: 'Работа в офисе',
        emoji: '💼',
        anchor: 'clock',
        start: '09:00',
        durationMin: 9 * 60,
        splitForLunch: true,
      },
    ],
    defaultNeeds: ['deep_work', 'chores', 'rest', 'sport'],
  },
  {
    id: 'remote',
    label: 'Удалённый специалист',
    emoji: '💻',
    description: 'Работаете из дома — больше гибкости, но и больше риска смешать работу с личным временем.',
    fixedBlocks: [
      {
        label: 'Рабочие фокус-блоки',
        emoji: '🖥️',
        anchor: 'clock',
        start: '10:00',
        durationMin: 8 * 60,
        splitForLunch: true,
      },
    ],
    defaultNeeds: ['deep_work', 'learning', 'sport', 'rest'],
  },
  {
    id: 'freelancer',
    label: 'Фрилансер / творческая работа',
    emoji: '🎨',
    description: 'Минимум жёстких рамок — день строится вокруг проектов, созвонов с клиентами и вдохновения.',
    fixedBlocks: [
      {
        label: 'Созвон с клиентами',
        emoji: '📞',
        anchor: 'clock',
        start: '11:00',
        durationMin: 60,
      },
    ],
    defaultNeeds: ['creativity', 'deep_work', 'social', 'rest'],
  },
  {
    id: 'parent',
    label: 'Родитель с детьми',
    emoji: '👨‍👩‍👧',
    description: 'День вращается вокруг режима детей: сборы утром, дела вечером, мало непрерывного времени на себя.',
    fixedBlocks: [
      {
        label: 'Сборы и отвод детей',
        emoji: '🎒',
        anchor: 'afterWake',
        start: 30,
        durationMin: 60,
      },
      {
        label: 'Время с детьми',
        emoji: '🧸',
        anchor: 'clock',
        start: '16:30',
        durationMin: 3 * 60,
      },
    ],
    defaultNeeds: ['family', 'chores', 'rest', 'deep_work'],
  },
  {
    id: 'entrepreneur',
    label: 'Предприниматель / руководитель',
    emoji: '🚀',
    description: 'Насыщенный день из встреч и решений — важно защитить время на стратегию и не выгореть.',
    fixedBlocks: [
      {
        label: 'Встречи и переговоры',
        emoji: '🤝',
        anchor: 'clock',
        start: '10:00',
        durationMin: 3 * 60,
      },
      {
        label: 'Операционные задачи',
        emoji: '📋',
        anchor: 'clock',
        start: '15:00',
        durationMin: 2.5 * 60,
      },
    ],
    defaultNeeds: ['deep_work', 'social', 'learning', 'rest'],
  },
  {
    id: 'athlete',
    label: 'Спортсмен / ЗОЖ-фокус',
    emoji: '🏋️',
    description: 'Тренировки и восстановление — приоритет дня, всё остальное подстраивается под них.',
    fixedBlocks: [],
    defaultNeeds: ['sport', 'rest', 'chores', 'learning'],
    weightOverrides: { sport: 4, rest: 2.5 },
  },
]

export function getRole(id: string): Role {
  const found = ROLES.find((r) => r.id === id)
  if (!found) throw new Error(`Unknown role: ${id}`)
  return found
}
