# Music bank (2026-11-25)

The user topped up Musicful by 300 units (valid for one week) and asked to generate the music ahead. 10 sound variants × 5 requests × 2 tracks = **100 tracks, 300 units** (≈30 units per album of 10 tracks = 10 albums). Each variant has its own instrumentation, so the albums do not all sound alike (the "repetitive content" risk). All in D minor pentatonic, so variants can also be mixed. Same quiet rules as before (no percussion, no swelling, one level).

**Update (same day, user decision):** no new instruments. Every prompt is our proven Musicful prompt (the SHOGUN one: shakuhachi + koto + warm drone, the same rules) with only the scene sentence and the mood changed per future theme, exactly as we did for each album before. 10 themes × 10 tracks:

yuki (snow, December), ryu (ceiling dragon), masamune (Date Masamune), kuma (bear), uma (war horse), yoroi (armor), koi, tsuru (crane), kitsune (fox), ronin-ii.

Checking: the user can check all tracks at once — long check videos with a timestamped track list, so any claim time maps to a track id.

Generation: helper session, branch `claude/music-bank-2026-11` (one folder per variant). Every album still gets its one-cycle Content ID check before upload.

## Result (2026-11-25)
96 tracks generated (start balance 292, final 4): 9 themes × 10 + 6 extra for yuki; **ronin-ii not generated** (balance). Branch `claude/music-bank-2026-11`.

Technical check (key by chroma, ebur128 LRA, 3-s RMS swell): **74 of 96 pass**. Compatible keys: D minor, G minor and their relative majors F / B♭. Rejected (off-key or swelling): kitsune 1635864 · koi 1635836, 1635837, 1635843 · kuma 1635807 · masamune 1635790, 1635793, 1635797 · ryu 1635776, 1635777, 1635781, 1635784, 1635785 (RYŪ only 5 good) · uma 1635816, 1635817 · yoroi 1635822, 1635823 · yuki 1635767, 1635771, 1635870, 1635871, 1635874. Rejected tracks may still serve as Short music.

Content ID: all 96 in three unlisted check videos (`CHECK-TIMESTAMPS.txt` maps every time to a track id).
