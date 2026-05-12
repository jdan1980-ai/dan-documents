import {
  AbsoluteFill,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { COLORS } from "../lib/constants";

const BG_IMG = "assets/scene8-brain-chest.png";

export const Scene8CTA: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const pushIn = interpolate(frame, [0, durationInFrames], [1, 1.04], {
    extrapolateRight: "clamp",
  });

  const wavePhase = Math.sin((frame - 2 * fps) / 6);
  const waveActive = frame >= 2 * fps && frame <= 5 * fps;
  const wavePawRotate = waveActive ? wavePhase * 18 : 0;

  const blinkStart = 5.5 * fps;
  const blinkPhase = interpolate(
    frame - blinkStart,
    [0, 8, 16],
    [1, 0.05, 1],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  const ctaTextFade = interpolate(frame, [0, 12], [0, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ background: "#1a1f2e" }}>
      <AbsoluteFill style={{ transform: `scale(${pushIn})` }}>
        <Img
          src={staticFile(BG_IMG)}
          onError={() => undefined}
          style={{ width: "100%", height: "100%", objectFit: "cover" }}
        />

        <PawWaveOverlay rotation={wavePawRotate} />
        <BlinkVeil alpha={1 - blinkPhase} />

        <CTAText alpha={ctaTextFade} />
        <FollowChip alpha={ctaTextFade} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const PawWaveOverlay: React.FC<{ rotation: number }> = ({ rotation }) => (
  <div
    style={{
      position: "absolute",
      left: "55%",
      top: "45%",
      width: 120,
      height: 120,
      transform: `rotate(${rotation}deg)`,
      transformOrigin: "50% 90%",
      fontSize: 96,
      filter: "drop-shadow(0 4px 12px rgba(0,0,0,0.4))",
      opacity: rotation === 0 ? 0 : 0.65,
      pointerEvents: "none",
    }}
  >
    ✋
  </div>
);

const BlinkVeil: React.FC<{ alpha: number }> = ({ alpha }) => {
  if (alpha <= 0) return null;
  return (
    <div
      style={{
        position: "absolute",
        left: "38%",
        top: "32%",
        width: 160,
        height: 24,
        borderRadius: 12,
        background: `rgba(20, 30, 40, ${alpha})`,
        pointerEvents: "none",
      }}
    />
  );
};

const CTAText: React.FC<{ alpha: number }> = ({ alpha }) => (
  <div
    style={{
      position: "absolute",
      bottom: "22%",
      left: 0,
      right: 0,
      display: "flex",
      justifyContent: "center",
      opacity: alpha,
    }}
  >
    <div
      style={{
        background: `linear-gradient(180deg, ${COLORS.electricYellow} 0%, #FFB347 100%)`,
        color: COLORS.charcoal,
        padding: "20px 56px",
        borderRadius: 999,
        fontFamily: "Inter, sans-serif",
        fontWeight: 900,
        fontSize: 56,
        letterSpacing: 1,
        textTransform: "uppercase",
        boxShadow: "0 16px 40px rgba(255,180,71,0.4)",
        border: "4px solid white",
      }}
    >
      Check tonight 🩷
    </div>
  </div>
);

const FollowChip: React.FC<{ alpha: number }> = ({ alpha }) => (
  <div
    style={{
      position: "absolute",
      bottom: "10%",
      left: 0,
      right: 0,
      display: "flex",
      justifyContent: "center",
      opacity: alpha,
    }}
  >
    <div
      style={{
        background: "rgba(0,0,0,0.78)",
        color: "white",
        padding: "14px 36px",
        borderRadius: 999,
        fontFamily: "Inter, sans-serif",
        fontWeight: 800,
        fontSize: 40,
        letterSpacing: 1,
        border: `3px solid ${COLORS.emeraldEye}`,
      }}
    >
      🐱 Follow Brain
    </div>
  </div>
);
