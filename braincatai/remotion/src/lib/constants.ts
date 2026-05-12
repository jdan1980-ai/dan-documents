export const FPS = 30;
export const WIDTH = 1080;
export const HEIGHT = 1920;

export const SCENE_DURATION_SEC = 7;
export const SCENE_FRAMES = SCENE_DURATION_SEC * FPS;

export const END_CARD_SEC = 3;
export const END_CARD_FRAMES = END_CARD_SEC * FPS;

export const TOTAL_SCENES = 8;
export const TOTAL_DURATION_FRAMES = TOTAL_SCENES * SCENE_FRAMES + END_CARD_FRAMES;

export const COLORS = {
  emeraldEye: "#3DDC84",
  electricYellow: "#FFD23F",
  warmAmber: "#FFB347",
  coolMoonlight: "#A8C5E0",
  pastelPink: "#FFB6C1",
  charcoal: "#1A1A1A",
  cream: "#F5E6D3",
} as const;
