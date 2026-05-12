import { interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { COLORS } from "./constants";

const MAX_WORDS_PER_CHUNK = 4;

function chunkLine(line: string): string[] {
  const words = line.replace(/\s+/g, " ").trim().split(" ");
  const chunks: string[] = [];
  for (let i = 0; i < words.length; i += MAX_WORDS_PER_CHUNK) {
    chunks.push(words.slice(i, i + MAX_WORDS_PER_CHUNK).join(" "));
  }
  return chunks;
}

export const Subtitles: React.FC<{ line: string }> = ({ line }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const chunks = chunkLine(line);
  const perChunkFrames = Math.floor(durationInFrames / chunks.length);
  const idx = Math.min(Math.floor(frame / perChunkFrames), chunks.length - 1);
  const localFrame = frame - idx * perChunkFrames;
  const fadeIn = interpolate(localFrame, [0, 4], [0, 1], {
    extrapolateRight: "clamp",
  });
  const fadeOut = interpolate(
    localFrame,
    [perChunkFrames - 6, perChunkFrames],
    [1, 0.7],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );
  const opacity = Math.min(fadeIn, fadeOut);

  return (
    <div
      style={{
        position: "absolute",
        top: "12%",
        left: 0,
        right: 0,
        display: "flex",
        justifyContent: "center",
        pointerEvents: "none",
        opacity,
      }}
    >
      <div
        style={{
          background: "rgba(0,0,0,0.78)",
          color: "white",
          padding: "18px 36px",
          borderRadius: 18,
          fontFamily: "Inter, sans-serif",
          fontWeight: 900,
          fontSize: 64,
          letterSpacing: 0.5,
          textTransform: "uppercase",
          textShadow: `0 0 16px ${COLORS.electricYellow}80`,
          maxWidth: "85%",
          textAlign: "center",
          lineHeight: 1.05,
        }}
      >
        {chunks[idx]}
      </div>
    </div>
  );
};
