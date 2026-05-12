import {
  AbsoluteFill,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { COLORS } from "../lib/constants";

const ZONES_BY_RANK = [
  { id: "chest", label: "ON CHEST", hearts: 5, x: 50, y: 32 },
  { id: "head", label: "BY HEAD", hearts: 4, x: 25, y: 48 },
  { id: "paw", label: "PAW TOUCH", hearts: 4, x: 75, y: 48 },
  { id: "legs", label: "BETWEEN LEGS", hearts: 4, x: 25, y: 68 },
  { id: "feet", label: "AT FEET", hearts: 3, x: 75, y: 68 },
  { id: "corner", label: "FAR CORNER", hearts: 2, x: 50, y: 85 },
];

const BG_IMG = "assets/scene3-brain-lab.png";

export const Scene3LabChart: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const sequencePulses = ZONES_BY_RANK.map((_, i) => {
    const start = (2 + i * 0.45) * fps;
    const dur = 14;
    return interpolate(frame - start, [0, dur / 2, dur], [0, 1, 0], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    });
  });

  return (
    <AbsoluteFill style={{ background: "#1f2935" }}>
      <Img
        src={staticFile(BG_IMG)}
        onError={() => undefined}
        style={{ width: "100%", height: "100%", objectFit: "cover" }}
      />
      <ChartPanel>
        {ZONES_BY_RANK.map((zone, i) => (
          <ZoneRow key={zone.id} zone={zone} glow={sequencePulses[i]} />
        ))}
      </ChartPanel>
    </AbsoluteFill>
  );
};

const ChartPanel: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div
    style={{
      position: "absolute",
      top: "6%",
      left: "8%",
      width: "84%",
      height: "52%",
      borderRadius: 32,
      background: "rgba(255, 250, 240, 0.92)",
      boxShadow: "0 20px 50px rgba(0,0,0,0.4)",
      padding: 28,
    }}
  >
    <div
      style={{
        textAlign: "center",
        fontFamily: "Inter, sans-serif",
        fontWeight: 800,
        fontSize: 36,
        color: COLORS.charcoal,
        marginBottom: 8,
        letterSpacing: 1,
      }}
    >
      TRUST SCORE BY POSITION
    </div>
    <div style={{ position: "relative", width: "100%", height: "85%" }}>
      {children}
    </div>
  </div>
);

const ZoneRow: React.FC<{
  zone: (typeof ZONES_BY_RANK)[number];
  glow: number;
}> = ({ zone, glow }) => {
  return (
    <div
      style={{
        position: "absolute",
        left: `${zone.x}%`,
        top: `${zone.y}%`,
        transform: "translate(-50%, -50%)",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: 2,
      }}
    >
      <div
        style={{
          fontFamily: "Inter, sans-serif",
          fontWeight: 700,
          fontSize: 22,
          color: COLORS.charcoal,
          textShadow:
            glow > 0
              ? `0 0 ${12 * glow}px rgba(255,160,200,${glow})`
              : "none",
        }}
      >
        {zone.label}
      </div>
      <div style={{ display: "flex", gap: 2 }}>
        {Array.from({ length: zone.hearts }).map((_, i) => (
          <span
            key={i}
            style={{
              fontSize: 22,
              transform: `scale(${1 + glow * 0.4})`,
              filter:
                glow > 0
                  ? `drop-shadow(0 0 ${8 * glow}px rgba(255,140,180,${glow}))`
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
