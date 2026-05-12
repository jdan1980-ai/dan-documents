import {
  AbsoluteFill,
  Img,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { COLORS, FPS } from "../lib/constants";

type Zone = {
  id: string;
  label: string;
  hearts: number;
  x: number;
  y: number;
};

const ZONES: Zone[] = [
  { id: "chest", label: "ON CHEST", hearts: 5, x: 50, y: 50 },
  { id: "head", label: "BY HEAD", hearts: 4, x: 50, y: 22 },
  { id: "legs", label: "BETWEEN LEGS", hearts: 4, x: 20, y: 55 },
  { id: "feet", label: "AT FEET", hearts: 3, x: 50, y: 80 },
  { id: "corner", label: "FAR CORNER", hearts: 2, x: 80, y: 80 },
  { id: "paw", label: "PAW TOUCH", hearts: 4, x: 80, y: 30 },
];

const BRAIN_IMG = "assets/scene4-brain-labcoat.png";
const PLACEHOLDER_BG = "linear-gradient(180deg, #2b3a4a 0%, #1a2330 100%)";

export const Scene4TopScore: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const t0 = 0;
  const t2 = 2 * fps;
  const t4 = 4 * fps;
  const t7 = 7 * fps;

  const pushIn = interpolate(frame, [t0, t7], [1, 1.07], {
    extrapolateRight: "clamp",
  });

  const chestSupersize = spring({
    frame: frame - t2,
    fps,
    config: { damping: 12, stiffness: 110 },
  });

  const dimOthers = interpolate(frame, [t2, t2 + 18], [1, 0.35], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const ribbonBounce = spring({
    frame: frame - (t2 + 6),
    fps,
    config: { damping: 8, stiffness: 140 },
  });

  const starburstPulse =
    Math.sin((frame - t2) / 6) * 0.08 + 1 + (frame >= t2 ? 0.25 : 0);

  return (
    <AbsoluteFill style={{ background: PLACEHOLDER_BG }}>
      <AbsoluteFill style={{ transform: `scale(${pushIn})` }}>
        <LabBackground />

        <BrainPlaceholder src={BRAIN_IMG} />

        <ChartFrame>
          {ZONES.map((zone) => {
            const isChest = zone.id === "chest";
            const opacity = isChest ? 1 : dimOthers;
            const scale = isChest
              ? 1 + chestSupersize * 0.6 * (starburstPulse - 1 + 0.25)
              : 1;

            return (
              <ZoneCard
                key={zone.id}
                zone={zone}
                opacity={opacity}
                scale={scale}
                isChest={isChest}
                burst={isChest ? chestSupersize : 0}
              />
            );
          })}
        </ChartFrame>

        {ribbonBounce > 0.01 ? (
          <TopScoreRibbon scale={ribbonBounce} />
        ) : null}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const LabBackground: React.FC = () => (
  <AbsoluteFill
    style={{
      background:
        "radial-gradient(ellipse at 50% 40%, rgba(255,200,140,0.18) 0%, rgba(0,0,0,0) 55%), linear-gradient(180deg, #2b3a4a 0%, #1a2330 100%)",
    }}
  />
);

const BrainPlaceholder: React.FC<{ src: string }> = ({ src }) => {
  return (
    <div
      style={{
        position: "absolute",
        bottom: 0,
        left: 0,
        right: 0,
        height: "45%",
        display: "flex",
        justifyContent: "center",
        alignItems: "flex-end",
      }}
    >
      <Img
        src={staticFile(src)}
        onError={() => undefined}
        style={{
          height: "100%",
          objectFit: "contain",
          opacity: 1,
        }}
      />
    </div>
  );
};

const ChartFrame: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div
    style={{
      position: "absolute",
      top: "8%",
      left: "8%",
      width: "84%",
      height: "48%",
      borderRadius: 36,
      background: "rgba(255, 250, 240, 0.94)",
      boxShadow: "0 24px 60px rgba(0,0,0,0.45)",
      padding: 24,
      overflow: "hidden",
    }}
  >
    <div
      style={{
        position: "relative",
        width: "100%",
        height: "100%",
        background:
          "linear-gradient(180deg, #fff7e8 0%, #ffe9c8 100%)",
        borderRadius: 20,
      }}
    >
      {children}
    </div>
  </div>
);

const ZoneCard: React.FC<{
  zone: Zone;
  opacity: number;
  scale: number;
  isChest: boolean;
  burst: number;
}> = ({ zone, opacity, scale, isChest, burst }) => {
  return (
    <div
      style={{
        position: "absolute",
        left: `${zone.x}%`,
        top: `${zone.y}%`,
        transform: `translate(-50%, -50%) scale(${scale})`,
        opacity,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: 4,
        textAlign: "center",
        transition: "all 100ms",
      }}
    >
      {isChest ? <Starburst burst={burst} /> : null}
      <div
        style={{
          fontFamily: "Inter, sans-serif",
          fontWeight: 800,
          fontSize: 28,
          color: COLORS.charcoal,
          textShadow: isChest ? "0 2px 12px rgba(255,150,180,0.6)" : "none",
          letterSpacing: 0.5,
        }}
      >
        {zone.label}
      </div>
      <div style={{ display: "flex", gap: 4 }}>
        {Array.from({ length: zone.hearts }).map((_, i) => (
          <span
            key={i}
            style={{
              fontSize: isChest ? 36 : 28,
              filter: isChest
                ? "drop-shadow(0 0 12px rgba(255,120,170,0.9))"
                : "none",
            }}
          >
            🩷
          </span>
        ))}
      </div>
    </div>
  );
};

const Starburst: React.FC<{ burst: number }> = ({ burst }) => (
  <div
    style={{
      position: "absolute",
      width: 240,
      height: 240,
      borderRadius: "50%",
      background:
        "radial-gradient(circle, rgba(255,180,210,0.85) 0%, rgba(255,180,210,0) 70%)",
      transform: `scale(${burst})`,
      zIndex: -1,
    }}
  />
);

const TopScoreRibbon: React.FC<{ scale: number }> = ({ scale }) => (
  <div
    style={{
      position: "absolute",
      top: "5%",
      left: "50%",
      transform: `translate(-50%, 0) scale(${scale})`,
      background:
        "linear-gradient(180deg, #ff9ec3 0%, #ff6fa3 100%)",
      color: "white",
      padding: "16px 48px",
      borderRadius: 999,
      fontFamily: "Inter, sans-serif",
      fontWeight: 900,
      fontSize: 48,
      letterSpacing: 2,
      boxShadow: "0 12px 32px rgba(255,100,160,0.55)",
      border: "4px solid white",
    }}
  >
    TOP SCORE
  </div>
);
