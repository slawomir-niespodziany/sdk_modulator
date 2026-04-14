# Project Context: Scientific Paper on Closed Loop Fiber Optic Gyroscope

## Topic
Scientific paper on **closed loop fiber optic gyroscope (FOG)**.

## Focus Area
**Modulator implementations**, covering both:
- **Hardware part**: physical modulator design, components, and implementation
- **Software part**: signal processing, control algorithms, and software-driven modulation

## Status
Work in progress. User will return after breaks — use this file to restore context.

## Paper Structure (in progress)
- `content.md` — main paper content file

### Sections written so far
1. **Introduction** — IFOG applications, Sagnac phase shift, importance of precision, modulator as critical component
2. **Electro-Optical Front-End** — IFOG construction (SLD, fiber coil, photodetector), cosine response, quadrature biasing, IOC (LiNbO₃), Pockels effect, Δφ = π·V/Vπ, Vπ drift, closed-loop dual role of modulator

### Key technical points established
- IOC is voltage-driven, high input impedance (capacitive load)
- Phase shift is highly linear (Pockels effect) — main concern is Vπ drift with temperature/aging, not intrinsic nonlinearity
- DC drift in LiNbO₃: charge migration under sustained voltage — push-pull (differential) drive mitigates but does not eliminate it
- IOC is a two-channel Mach-Zehnder structure: two arms with individual electrodes, Y-junction splitter/combiner, integrated polarizer
- Push-pull drive: halves Vπ (doubles efficiency) and reduces DC drift by keeping net E-field near zero

### Open questions / notes
- "DOES IT???" marker in content.md Notes section — partially resolved: push-pull does help with DC drift but doesn't eliminate it
- Vπ drift compensation strategy not yet discussed in paper

## Next steps (suggested)
- Hardware section: modulator driver circuit design
- Software section: closed-loop control, digital phase ramp, demodulation
