import {
  AbsoluteFill,
  Audio,
  Sequence,
  Video,
  staticFile,
} from "remotion";
import { END_CARD_FRAMES, SCENE_FRAMES } from "./lib/constants";
import { SCENES } from "./lib/script";
import { Subtitles } from "./lib/Subtitles";
import { Scene2BedSurvey } from "./scenes/Scene2BedSurvey";
import { Scene3LabChart } from "./scenes/Scene3LabChart";
import { Scene4TopScore } from "./scenes/Scene4TopScore";
import { Scene7PawAnchor } from "./scenes/Scene7PawAnchor";

const REMOTION_COMPONENTS = {
  Scene2BedSurvey,
  Scene3LabChart,
  Scene4TopScore,
  Scene7PawAnchor,
} as const;

export const Main: React.FC = () => {
  return (
    <AbsoluteFill style={{ background: "black" }}>
      <Audio src={staticFile("audio/vo.mp3")} volume={1.0} />
      <Audio src={staticFile("audio/music.mp3")} volume={0.18} />

      {SCENES.map((scene, i) => (
        <Sequence
          key={scene.num}
          from={i * SCENE_FRAMES}
          durationInFrames={SCENE_FRAMES}
          name={`Scene ${scene.num} — ${scene.title}`}
        >
          <AbsoluteFill>
            {scene.source.kind === "veo" ? (
              <Video
                src={staticFile(scene.source.clipFile)}
                style={{ width: "100%", height: "100%", objectFit: "cover" }}
              />
            ) : (
              (() => {
                const Comp = REMOTION_COMPONENTS[scene.source.componentId];
                return <Comp />;
              })()
            )}
            <Subtitles line={scene.vo} />
          </AbsoluteFill>
        </Sequence>
      ))}

      <Sequence
        from={SCENES.length * SCENE_FRAMES}
        durationInFrames={END_CARD_FRAMES}
        name="End card"
      >
        <EndCard />
      </Sequence>
    </AbsoluteFill>
  );
};

const EndCard: React.FC = () => (
  <AbsoluteFill
    style={{
      background:
        "radial-gradient(ellipse at center, #2a3550 0%, #0f1320 100%)",
      justifyContent: "center",
      alignItems: "center",
      gap: 32,
    }}
  >
    <div
      style={{
        fontFamily: "Inter, sans-serif",
        fontWeight: 900,
        fontSize: 120,
        color: "white",
        textShadow: "0 0 32px rgba(61,220,132,0.6)",
      }}
    >
      🐱
    </div>
    <div
      style={{
        fontFamily: "Inter, sans-serif",
        fontWeight: 900,
        fontSize: 64,
        color: "white",
        letterSpacing: 2,
      }}
    >
      FOLLOW BRAIN
    </div>
    <div
      style={{
        fontFamily: "Inter, sans-serif",
        fontWeight: 600,
        fontSize: 36,
        color: "#FFD23F",
      }}
    >
      for more cat secrets
    </div>
  </AbsoluteFill>
);

