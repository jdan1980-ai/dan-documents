export type SceneSource =
  | { kind: "veo"; clipFile: string }
  | { kind: "remotion"; componentId: SceneId };

export type SceneId =
  | "Scene2BedSurvey"
  | "Scene3LabChart"
  | "Scene4TopScore"
  | "Scene7PawAnchor"
  | "Scene8CTA";

export type Scene = {
  num: number;
  title: string;
  vo: string;
  source: SceneSource;
};

export const SCENES: Scene[] = [
  {
    num: 1,
    title: "Hook on chest",
    vo: "Your cat just claimed your CHEST. WHERE they sleep on you tells the whole story.",
    source: { kind: "veo", clipFile: "clips/scene1-hook.mp4" },
  },
  {
    num: 2,
    title: "Bed survey",
    vo: "Because every spot on your bed means something different.",
    source: { kind: "remotion", componentId: "Scene2BedSurvey" },
  },
  {
    num: 3,
    title: "Scientist Brain + chart",
    vo: "Cats rank you by distance. Closer equals more trust.",
    source: { kind: "remotion", componentId: "Scene3LabChart" },
  },
  {
    num: 4,
    title: "TOP SCORE reveal",
    vo: "On your CHEST? Top score. They want your heartbeat — just like their mom's.",
    source: { kind: "remotion", componentId: "Scene4TopScore" },
  },
  {
    num: 5,
    title: "Scent shimmer at head",
    vo: "By your head? They're stealing your scent. To them, you smell like home.",
    source: { kind: "veo", clipFile: "clips/scene5-scent.mp4" },
  },
  {
    num: 6,
    title: "Slow-mo pull-back twist",
    vo: "At the FAR end of the bed? Still huge. They picked your bed over being alone.",
    source: { kind: "veo", clipFile: "clips/scene6-twist.mp4" },
  },
  {
    num: 7,
    title: "Paw on wrist anchor",
    vo: "And that one paw touching you? It's an anchor. They need to feel you breathe.",
    source: { kind: "remotion", componentId: "Scene7PawAnchor" },
  },
  {
    num: 8,
    title: "CTA wave + meow",
    vo: "Check tonight. Where does YOUR cat sleep? Follow Brain for more cat secrets.",
    source: { kind: "remotion", componentId: "Scene8CTA" },
  },
];
