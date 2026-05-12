import {
  AbsoluteFill,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { COLORS } from "../lib/constants";

const BG_IMG = "assets/scene7-paw-wrist.png";
const BREATHS_PER_SEC = 0.22;

export const Scene7PawAnchor: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const pushIn = interpolate(frame, [0, durationInFrames], [1, 1.03], {
    extrapolateRight: "clamp",
  });

  const breathPhase = Math.sin((frame / fps) * BREATHS_PER_SEC * Math.PI * 2);
  const breathOffset = breathPhase * 8;

  const glowPulse = 0.6 + Math.abs(breathPhase) * 0.4;

  const sparkleStart = 5 * fps;
  const sparkleAlpha = interpolate(
    frame - sparkleStart,
    [0, 8, 22],
    [0, 1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  return (
    <AbsoluteFill style={{ background: "#241a1a" }}>
      <AbsoluteFill
        style={{
          transform: `scale(${pushIn}) translateY(${breathOffset}px)`,
        }}
      >
        <Img
          src={staticFile(BG_IMG)}
          onError={() => undefined}
          style={{ width: "100%", height: "100%", objectFit: "cover" }}
        />
        <AnchorGlow alpha={glowPulse} />
        {sparkleAlpha > 0 ? <HeartSparkle alpha={sparkleAlpha} /> : null}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const AnchorGlow: React.FC<{ alpha: number }> = ({ alpha }) => (
  <div
    style={{
      position: "absolute",
      left: "50%",
      top: "55%",
      transform: "translate(-50%, -50%)",
      width: 280,
      height: 280,
      borderRadius: "50%",
      background: `radial-gradient(circle, ${COLORS.pastelPink}cc 0%, ${COLORS.pastelPink}00 65%)`,
      opacity: alpha,
      filter: "blur(4px)",
      mixBlendMode: "screen",
    }}
  />
);

const HeartSparkle: React.FC<{ alpha: number }> = ({ alpha }) => (
  <div
    style={{
      position: "absolute",
      right: "18%",
      top: "32%",
      fontSize: 64,
      opacity: alpha,
      filter: `drop-shadow(0 0 16px rgba(255,140,180,${alpha}))`,
      transform: `scale(${0.8 + alpha * 0.4})`,
    }}
  >
    💖
  </div>
);
