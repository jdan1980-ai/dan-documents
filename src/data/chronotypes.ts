import type { Chronotype } from '../types'

const H = 60

export const CHRONOTYPES: Chronotype[] = [
  {
    id: 'lark',
    label: 'Жаворонок',
    emoji: '🌅',
    tagline: 'Рано встаёте — рано мыслите ясно',
    description:
      'Пик энергии приходится на утро. Лучше всего справляетесь со сложными задачами до обеда, вечером быстро устаёте.',
    defaultWake: '06:00',
    defaultSleep: '22:00',
    energy: [
      { startMin: 0, endMin: 6 * H, level: 'low' },
      { startMin: 6 * H, endMin: 10 * H, level: 'high' },
      { startMin: 10 * H, endMin: 12 * H, level: 'medium' },
      { startMin: 12 * H, endMin: 14 * H, level: 'low' },
      { startMin: 14 * H, endMin: 17 * H, level: 'medium' },
      { startMin: 17 * H, endMin: 22 * H, level: 'low' },
      { startMin: 22 * H, endMin: 24 * H, level: 'low' },
    ],
  },
  {
    id: 'dove',
    label: 'Голубь',
    emoji: '🌤️',
    tagline: 'Гибкий ритм, два пика продуктивности',
    description:
      'Промежуточный хронотип — комфортно и утром, и днём. Есть чёткий утренний пик и более мягкий во второй половине дня.',
    defaultWake: '07:00',
    defaultSleep: '23:00',
    energy: [
      { startMin: 0, endMin: 7 * H, level: 'low' },
      { startMin: 7 * H, endMin: 9 * H, level: 'medium' },
      { startMin: 9 * H, endMin: 12 * H, level: 'high' },
      { startMin: 12 * H, endMin: 14 * H, level: 'low' },
      { startMin: 14 * H, endMin: 16 * H, level: 'medium' },
      { startMin: 16 * H, endMin: 19 * H, level: 'high' },
      { startMin: 19 * H, endMin: 22 * H, level: 'medium' },
      { startMin: 22 * H, endMin: 24 * H, level: 'low' },
    ],
  },
  {
    id: 'owl',
    label: 'Сова',
    emoji: '🌙',
    tagline: 'Раскачиваетесь долго, зато вечером — огонь',
    description:
      'Утро — не ваше время: телу нужно раскачаться. Настоящий фокус и творческий подъём приходят ближе к вечеру и ночью.',
    defaultWake: '09:00',
    defaultSleep: '01:00',
    energy: [
      { startMin: 0, endMin: 1 * H, level: 'high' },
      { startMin: 1 * H, endMin: 8 * H, level: 'low' },
      { startMin: 8 * H, endMin: 11 * H, level: 'low' },
      { startMin: 11 * H, endMin: 14 * H, level: 'medium' },
      { startMin: 14 * H, endMin: 16 * H, level: 'low' },
      { startMin: 16 * H, endMin: 19 * H, level: 'medium' },
      { startMin: 19 * H, endMin: 23 * H, level: 'high' },
      { startMin: 23 * H, endMin: 24 * H, level: 'high' },
    ],
  },
]

export function getChronotype(id: string): Chronotype {
  const found = CHRONOTYPES.find((c) => c.id === id)
  if (!found) throw new Error(`Unknown chronotype: ${id}`)
  return found
}
