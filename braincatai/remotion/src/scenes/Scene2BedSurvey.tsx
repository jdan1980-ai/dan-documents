import {
  AbsoluteFill,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { COLORS } from "../lib/constants";

type GlowZone = {
  id: string;
  x: number;
  y: number;
  pulseAtSec: number;
};

const ZONES: GlowZone[] = [
  { id: "pillow", x: 30, y: 28, pulseAtSec: 0.3 },
  { id: "chest", x: 50, y: 50, pulseAtSec: 1.2 },
  { id: "foot", x: 70, y: 72, pulseAtSec: 2.4 },
  { id: "corner", x: 22, y: 78, pulseAtSec: 3.5 },
];

const BG_IMG = "assets/scene2-bed-bg.png";

export const Scene2BedSurvey: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const pullBack = interpolate(frame, [0, durationInFrames], [1.04, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ background: "#1a2330" }}>
      <AbsoluteFill style={{ transform: `scale(${pullBack})` }}>
        <Img
          src={staticFile(BG_IMG)}
          onError={() => undefined}
          style={{ width: "100%", height: "100%", objectFit: "cover" }}
        />
        {ZONES.map((zone) => (
          <GlowCircle key={zone.id} zone={zone} fps={fps} frame={frame} />
        ))}
        <FinalUnisonPulse frame={frame} fps={fps} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const GlowCircle: React.FC<{
  zone: GlowZone;
  fps: number;
  frame: number;
}> = ({ zone, fps, frame }) => {
  const pulseFrame = zone.pulseAtSec * fps;
  const pulseDuration = 18;
  const localFrame = frame - pulseFrame;

  const opacity = interpolate(
    localFrame,
    [0, pulseDuration / 2, pulseDuration],
    [0.25, 0.9, 0.25],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  const scale = interpolate(
    localFrame,
    [0, pulseDuration / 2, pulseDuration],
    [0.8, 1.2, 1],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  return (
    <div
      style={{
        position: "absolute",
        left: `${zone.x}%`,
        top: `${zone.y}%`,
        transform: `translate(-50%, -50%) scale(${scale})`,
        width: 180,
        height: 180,
        borderRadius: "50%",
        background: `radial-gradient(circle, ${COLORS.electricYellow}cc 0%, ${COLORS.electricYellow}00 70%)`,
        opacity,
        filter: "blur(2px)",
      }}
    />
  );
};

const FinalUnisonPulse: React.FC<{ frame: number; fps: number }> = ({
  frame,
  fps,
}) => {
  const startFrame = 5 * fps;
  const localFrame = frame - startFrame;
  const opacity = interpolate(localFrame, [0, 10, 25], [0, 0.8, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  if (opacity <= 0) return null;

  return (
    <>
      {ZONES.map((zone) => (
        <div
          key={`final-${zone.id}`}
          style={{
            position: "absolute",
            left: `${zone.x}%`,
            top: `${zone.y}%`,
            transform: "translate(-50%, -50%)",
            width: 220,
            height: 220,
            borderRadius: "50%",
            background: `radial-gradient(circle, ${COLORS.electricYellow}aa 0%, ${COLORS.electricYellow}00 70%)`,
            opacity,
          }}
        />
      ))}
    </>
  );
};
