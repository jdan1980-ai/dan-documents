import { Composition } from "remotion";
import {
  FPS,
  WIDTH,
  HEIGHT,
  SCENE_FRAMES,
  TOTAL_DURATION_FRAMES,
} from "./lib/constants";
import { Main } from "./Main";
import { Scene2BedSurvey } from "./scenes/Scene2BedSurvey";
import { Scene3LabChart } from "./scenes/Scene3LabChart";
import { Scene4TopScore } from "./scenes/Scene4TopScore";
import { Scene7PawAnchor } from "./scenes/Scene7PawAnchor";

export const Root: React.FC = () => {
  return (
    <>
      <Composition
        id="MainComposition"
        component={Main}
        durationInFrames={TOTAL_DURATION_FRAMES}
        fps={FPS}
        width={WIDTH}
        height={HEIGHT}
      />
      <Composition
        id="Scene2BedSurvey"
        component={Scene2BedSurvey}
        durationInFrames={SCENE_FRAMES}
        fps={FPS}
        width={WIDTH}
        height={HEIGHT}
      />
      <Composition
        id="Scene3LabChart"
        component={Scene3LabChart}
        durationInFrames={SCENE_FRAMES}
        fps={FPS}
        width={WIDTH}
        height={HEIGHT}
      />
      <Composition
        id="Scene4TopScore"
        component={Scene4TopScore}
        durationInFrames={SCENE_FRAMES}
        fps={FPS}
        width={WIDTH}
        height={HEIGHT}
      />
      <Composition
        id="Scene7PawAnchor"
        component={Scene7PawAnchor}
        durationInFrames={SCENE_FRAMES}
        fps={FPS}
        width={WIDTH}
        height={HEIGHT}
      />
    </>
  );
};
