# Поиск щелчков: резкие скачки второй разности сигнала относительно локального фона
# Запуск:  pwsh -File find_clicks.ps1 -Path track.wav
param([Parameter(Mandatory)][string]$Path)

Add-Type -TypeDefinition @"
using System;
using System.IO;
using System.Text;
using System.Collections.Generic;

public static class ClickFinder
{
    public static string Run(string path)
    {
        byte[] b = File.ReadAllBytes(path);
        int sr = BitConverter.ToInt32(b, 24), ch = BitConverter.ToInt16(b, 22);
        int n = (b.Length - 44) / (2 * ch);
        var sb = new StringBuilder();
        var times = new List<double>();
        for (int c = 0; c < ch; c++)
        {
            double[] d = new double[n];
            Func<int, double> s = i => BitConverter.ToInt16(b, 44 + (i * ch + c) * 2) / 32768.0;
            for (int i = 2; i < n; i++) d[i] = Math.Abs(s(i) - 2 * s(i - 1) + s(i - 2));
            int win = sr / 20;   // фон по окну 50 мс
            double acc = 0;
            for (int i = 0; i < win; i++) acc += d[i];
            int last = -sr;
            for (int i = win; i < n - win; i++)
            {
                acc += d[i + win / 2] - d[i - win / 2];
                double bg = acc / win;
                if (d[i] > 12 * bg + 2e-4 && i - last > sr / 4)
                {
                    times.Add((double)i / sr); last = i;
                }
            }
        }
        times.Sort();
        sb.AppendLine("Найдено щелчков: " + times.Count);
        foreach (var t in times) sb.AppendLine(string.Format("  {0:F3} с", t));
        return sb.ToString();
    }
}
"@

[ClickFinder]::Run((Resolve-Path $Path).Path)
