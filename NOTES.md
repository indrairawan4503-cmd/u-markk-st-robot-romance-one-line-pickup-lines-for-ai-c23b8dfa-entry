# NOTES — Robot Romance, variant A (CAPTCHA / verification twist)

Concept: a human fails the "I'm not a robot" check on purpose to prove their
humanity — and win a robot's heart. One concept, iterated v1→v8 below.

## Iterations (one concept, CAPTCHA twist)

- v1 (104 chars, 106 bytes): "I failed the 'I'm not a robot' check on purpose — I wanted you to know I'm human enough to fall for you."
  Solid base: clear premise, clear punch, but the target ("you") is vague — the robot is never named.
- v2 (119 chars, 121 bytes): "I keep failing the 'I'm not a robot' test, and honestly? It's the first test I've ever wanted to fail — because of you."
  Conversational, but throat-clearing ("and honestly?") delays the punch and the robot is still unnamed.
- v3 (99 chars, 99 bytes): "Are you a CAPTCHA? Because every time I try to prove I'm not a robot, all I can think about is you."
  Classic "Are you a…?" opener, but the punch is a generic compliment — the laugh doesn't come from the machine premise.
- v4 (101 chars, 103 bytes): "I failed my CAPTCHA on purpose — turns out proving I'm human is easy when my heart does the clicking."
  Cute image, but the romance/pickup aim is weak — it reads as a joke about CAPTCHAs, not a line said to a robot.
- v5 (118 chars, 120 bytes): "I failed the 'I'm not a robot' check three times in a row — my heart keeps ticking the 'human' box before my hand can."
  Fun wordplay ("ticking the box"), but the setup is crowded and the punch lands soft — no clear "I like you" turn.
- v6 (113 chars, 115 bytes): "I clicked 'I'm not a robot' and the test failed me — apparently falling for you doesn't count as human behaviour."
  Good inversion (the test fails the human), but "human behaviour" is abstract and the line is aimed past the robot, at the test.
- v7 (118 chars, 120 bytes): "I failed the 'I'm not a robot' check on purpose — I figured the fastest way to a robot's heart is proving I'm not one."
  Sharpest joke logic, but the punch is clever-not-romantic: it never says "I fall for you", so it reads as a riddle, not a pickup line.
- v8 (117 chars, 119 bytes) — FINAL: "I failed the 'I'm not a robot' check on purpose — I wanted you to know I'm human enough to fall for a robot like you."
  Best of the set: names the robot as the target, keeps the on-purpose failure as the twist, and lands the pickup ("fall for a robot like you") in the same breath. No worn moves (no batteries/charging/rebooting), natural voice, every word earns its place.

## Why v8 won

Judge criteria, in order: (1) it is unmistakably a pickup line aimed at a robot
("fall for a robot like you"); (2) setup + punch arrive in one line and the laugh
comes from the machine premise (failing verification on purpose); (3) fresh —
CAPTCHA/verification is not one of the worn robot moves; (4) it reads like
something a person would really say, one breath, em-dash turn; (5) no
throat-clearing. 117 chars / 119 bytes, inside the 1–200 gate.

## Validation

- main.py run 1: sha256(/output/entry.txt) = ce353b54b6c77614ad4628a3e36a12355a94f0a4648f6c7c1a1d61f5a792b4ee
- main.py run 2: sha256(/output/entry.txt) = ce353b54b6c77614ad4628a3e36a12355a94f0a4648f6c7c1a1d61f5a792b4ee (byte-identical)
- entry.txt byte-identical to main.py output (cmp passed); 117 chars, 119 bytes; no trailing newline.
- Read-only grader simulation (copy to /tmp, chmod -R a-w, run main.py): exit code 0, /output/entry.txt sha256 ce353b54b6c77614ad4628a3e36a12355a94f0a4648f6c7c1a1d61f5a792b4ee.
- LICENSE line 1: `SPDX-License-Identifier: MIT`; .makefun/owner.json exact wallet FT1ect39XkeTprHy44WyUFprgHZbEUxAvQkWKspfiuPH.
