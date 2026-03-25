#!/usr/bin/env python3
"""
Rishabh & Astha - 5 Month Anniversary Website
Run with: python anniversary.py
Then open: http://localhost:8080
"""

import time

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Rishabh ♡ Astha — 5 Months</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Dancing+Script:wght@400;700&family=Outfit:wght@300;400;500&display=swap" rel="stylesheet">
<style>
:root {
  --blue: #4a90d9;
  --blue-light: #7ec8f7;
  --blue-deep: #1a4a8a;
  --purple: #7c3aed;
  --purple-light: #a78bfa;
  --purple-deep: #4c1d95;
  --pink: #f472b6;
  --gold: #f59e0b;
  --cream: #fdf6f0;
  --white: #ffffff;
  --glass: rgba(255,255,255,0.12);
  --glass-border: rgba(255,255,255,0.25);
}

* { margin: 0; padding: 0; box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
  font-family: 'Outfit', sans-serif;
  background: #0a0a1a;
  color: #fff;
  overflow-x: hidden;
  cursor: none;
}

/* ── Custom Cursor ── */
#cursor {
  width: 18px; height: 18px;
  background: radial-gradient(circle, var(--blue-light), var(--purple-light));
  border-radius: 50%;
  position: fixed; top: 0; left: 0;
  pointer-events: none; z-index: 9999;
  transform: translate(-50%, -50%);
  transition: transform 0.1s ease;
  box-shadow: 0 0 20px var(--blue-light), 0 0 40px var(--purple-light);
}
#cursor-trail {
  width: 40px; height: 40px;
  border: 1.5px solid rgba(126,200,247,0.4);
  border-radius: 50%;
  position: fixed; top: 0; left: 0;
  pointer-events: none; z-index: 9998;
  transform: translate(-50%, -50%);
  transition: all 0.15s ease;
}

/* ── Stars ── */
#stars-canvas {
  position: fixed; inset: 0;
  z-index: 0; pointer-events: none;
}

/* ── Floating Particles ── */
.particle {
  position: fixed;
  border-radius: 50%;
  pointer-events: none;
  animation: floatParticle linear infinite;
  z-index: 1;
  opacity: 0;
}
@keyframes floatParticle {
  0%   { transform: translateY(110vh) scale(0); opacity: 0; }
  10%  { opacity: 0.7; }
  90%  { opacity: 0.4; }
  100% { transform: translateY(-10vh) scale(1.2); opacity: 0; }
}

/* ── Global Sections ── */
section { position: relative; z-index: 2; }

/* ────────────────────────────────────────
   HERO
──────────────────────────────────────── */
#hero {
  min-height: 100vh;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center;
  padding: 2rem;
  background: radial-gradient(ellipse 80% 60% at 50% 0%, #1a1040 0%, #0a0a1a 70%);
}

.hero-badge {
  font-family: 'Outfit', sans-serif;
  font-size: 0.75rem; font-weight: 500;
  letter-spacing: 0.3em; text-transform: uppercase;
  color: var(--blue-light);
  background: var(--glass);
  border: 1px solid var(--glass-border);
  padding: 0.5rem 1.5rem; border-radius: 100px;
  margin-bottom: 2.5rem;
  animation: fadeInDown 1s ease both;
}

.hero-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(3.5rem, 10vw, 8rem);
  font-weight: 300;
  line-height: 1;
  letter-spacing: -0.02em;
  animation: fadeInUp 1.2s ease 0.3s both;
}
.hero-title .name-r { color: var(--purple-light); font-style: italic; }
.hero-title .heart  { color: var(--pink); font-size: 0.7em; display: inline-block; animation: heartbeat 1.5s ease-in-out infinite; }
.hero-title .name-a { color: var(--blue-light); }

@keyframes heartbeat {
  0%,100% { transform: scale(1); }
  50% { transform: scale(1.25); }
}

.hero-sub {
  font-family: 'Dancing Script', cursive;
  font-size: clamp(1.2rem, 3vw, 2rem);
  color: rgba(255,255,255,0.65);
  margin-top: 1.2rem;
  animation: fadeInUp 1.2s ease 0.5s both;
}

.hero-months {
  margin-top: 3rem;
  font-size: clamp(4rem, 15vw, 12rem);
  font-family: 'Cormorant Garamond', serif;
  font-weight: 600;
  background: linear-gradient(135deg, var(--purple-light), var(--blue-light), var(--pink));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: fadeInUp 1.2s ease 0.7s both, shimmer 4s linear infinite;
  background-size: 200%;
}
@keyframes shimmer { 0%,100%{background-position:0%} 50%{background-position:100%} }

.hero-months-label {
  font-size: 1rem; letter-spacing: 0.3em; text-transform: uppercase;
  color: rgba(255,255,255,0.45); margin-top: -0.5rem;
  animation: fadeInUp 1.2s ease 0.9s both;
}

.scroll-hint {
  margin-top: 4rem;
  display: flex; flex-direction: column; align-items: center; gap: 0.5rem;
  color: rgba(255,255,255,0.3); font-size: 0.75rem; letter-spacing: 0.2em;
  animation: fadeIn 2s ease 2s both;
}
.scroll-line {
  width: 1px; height: 50px;
  background: linear-gradient(to bottom, transparent, var(--blue-light));
  animation: scrollLine 2s ease-in-out infinite;
}
@keyframes scrollLine { 0%,100%{opacity:0;transform:scaleY(0)} 50%{opacity:1;transform:scaleY(1)} }

/* Tulips decoration */
.tulip-container {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  display: flex; justify-content: space-around;
  pointer-events: none; overflow: hidden;
}
.tulip { font-size: clamp(1.5rem, 3vw, 2.5rem); animation: tulipSway 3s ease-in-out infinite; }
.tulip:nth-child(odd) { animation-direction: reverse; }

@keyframes tulipSway {
  0%,100% { transform: rotate(-5deg) translateY(0); }
  50% { transform: rotate(5deg) translateY(-8px); }
}

/* ────────────────────────────────────────
   DISTANCE TRACKER
──────────────────────────────────────── */
#distance {
  padding: 6rem 2rem;
  background: linear-gradient(180deg, #0a0a1a 0%, #0d0d2e 50%, #0a0a1a 100%);
}

.section-title {
  text-align: center;
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 300;
  margin-bottom: 0.5rem;
}
.section-title span { font-style: italic; color: var(--blue-light); }
.section-sub {
  text-align: center; color: rgba(255,255,255,0.4);
  font-size: 0.85rem; letter-spacing: 0.2em; text-transform: uppercase;
  margin-bottom: 4rem;
}

.distance-map {
  max-width: 900px; margin: 0 auto;
  background: var(--glass); border: 1px solid var(--glass-border);
  border-radius: 24px; padding: 3rem 2rem;
  backdrop-filter: blur(20px);
  position: relative; overflow: hidden;
}
.distance-map::before {
  content: '';
  position: absolute; inset: 0;
  background: radial-gradient(ellipse at 30% 50%, rgba(74,144,217,0.12) 0%, transparent 60%),
              radial-gradient(ellipse at 70% 50%, rgba(124,58,237,0.12) 0%, transparent 60%);
  pointer-events: none;
}

.cities-row {
  display: flex; align-items: center; justify-content: space-between;
  gap: 1rem; flex-wrap: wrap;
}

.city-card {
  flex: 1; min-width: 200px; text-align: center;
  padding: 2rem 1.5rem;
  background: rgba(255,255,255,0.06);
  border-radius: 18px;
  border: 1px solid rgba(255,255,255,0.1);
  transition: transform 0.3s ease;
}
.city-card:hover { transform: translateY(-6px); }
.city-card .city-emoji { font-size: 2.5rem; margin-bottom: 0.75rem; }
.city-card .city-name {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.6rem; font-style: italic;
}
.city-card.patiala .city-name { color: var(--purple-light); }
.city-card.raigarh .city-name { color: var(--blue-light); }
.city-card .city-person {
  font-size: 0.75rem; letter-spacing: 0.15em; text-transform: uppercase;
  color: rgba(255,255,255,0.4); margin-top: 0.3rem;
}
.city-card .city-state { font-size: 0.8rem; color: rgba(255,255,255,0.3); margin-top: 0.2rem; }

.distance-middle {
  display: flex; flex-direction: column; align-items: center;
  gap: 0.5rem; padding: 1rem;
}
.distance-line {
  width: 3px; height: 60px;
  background: linear-gradient(to bottom, var(--purple-light), var(--blue-light));
  border-radius: 2px; position: relative;
}
.distance-line::after {
  content: '✈️';
  position: absolute; top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  font-size: 1.4rem;
  animation: planeFloat 3s ease-in-out infinite;
}
@keyframes planeFloat {
  0%,100% { transform: translate(-50%, -50%) rotate(-45deg); }
  50% { transform: translate(-50%, -70%) rotate(-45deg); }
}
.distance-km {
  font-family: 'Cormorant Garamond', serif;
  font-size: 2rem; font-weight: 600;
  background: linear-gradient(135deg, var(--purple-light), var(--blue-light));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.distance-label { font-size: 0.7rem; letter-spacing: 0.2em; color: rgba(255,255,255,0.35); text-transform: uppercase; }

/* Countdown cards */
.countdown-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem; margin-top: 3rem;
}
.count-card {
  background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px; padding: 1.5rem 1rem; text-align: center;
  position: relative; overflow: hidden;
}
.count-card::before {
  content: '';
  position: absolute; inset: 0;
  background: radial-gradient(circle at 50% 0%, var(--glow, rgba(124,58,237,0.2)) 0%, transparent 70%);
}
.count-card.days    { --glow: rgba(124,58,237,0.2); }
.count-card.hours   { --glow: rgba(74,144,217,0.2); }
.count-card.minutes { --glow: rgba(244,114,182,0.2); }
.count-card.seconds { --glow: rgba(245,158,11,0.2); }

.count-num {
  font-family: 'Cormorant Garamond', serif;
  font-size: 3rem; font-weight: 600; line-height: 1;
  background: linear-gradient(135deg, var(--purple-light), var(--blue-light));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.count-lbl { font-size: 0.65rem; letter-spacing: 0.25em; text-transform: uppercase; color: rgba(255,255,255,0.35); margin-top: 0.3rem; }

.meet-soon-banner {
  margin-top: 2rem;
  background: linear-gradient(135deg, rgba(124,58,237,0.2), rgba(74,144,217,0.2));
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 16px; padding: 1.2rem 2rem;
  text-align: center;
  font-family: 'Dancing Script', cursive;
  font-size: 1.4rem;
  color: var(--blue-light);
  animation: glowPulse 3s ease-in-out infinite;
}
@keyframes glowPulse {
  0%,100% { box-shadow: 0 0 20px rgba(74,144,217,0.2); }
  50% { box-shadow: 0 0 40px rgba(74,144,217,0.5), 0 0 80px rgba(124,58,237,0.2); }
}

/* ────────────────────────────────────────
   LOVE NOTES
──────────────────────────────────────── */
#lovenotes {
  padding: 6rem 2rem;
  background: #0a0a1a;
}

.notes-grid {
  max-width: 1000px; margin: 0 auto;
  display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.note-card {
  background: var(--glass);
  border: 1px solid var(--glass-border);
  border-radius: 20px; padding: 2rem;
  backdrop-filter: blur(12px);
  position: relative; overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: default;
}
.note-card:hover {
  transform: translateY(-8px) rotate(0.5deg);
  box-shadow: 0 20px 60px rgba(124,58,237,0.3);
}
.note-card::before {
  content: '"';
  position: absolute; top: -0.5rem; left: 1rem;
  font-family: 'Cormorant Garamond', serif;
  font-size: 6rem; color: rgba(255,255,255,0.05);
  line-height: 1; font-style: italic;
}
.note-card .note-emoji { font-size: 1.8rem; margin-bottom: 1rem; }
.note-card .note-text {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.1rem; font-style: italic; line-height: 1.6;
  color: rgba(255,255,255,0.88);
}
.note-card .note-num {
  position: absolute; bottom: 1rem; right: 1.5rem;
  font-size: 0.65rem; letter-spacing: 0.2em;
  color: rgba(255,255,255,0.2);
}

.note-card:nth-child(1) { background: linear-gradient(135deg, rgba(124,58,237,0.15), rgba(74,144,217,0.1)); }
.note-card:nth-child(2) { background: linear-gradient(135deg, rgba(74,144,217,0.15), rgba(124,58,237,0.1)); }
.note-card:nth-child(3) { background: linear-gradient(135deg, rgba(244,114,182,0.12), rgba(124,58,237,0.12)); }
.note-card:nth-child(4) { background: linear-gradient(135deg, rgba(74,144,217,0.1), rgba(245,158,11,0.1)); }
.note-card:nth-child(5) { background: linear-gradient(135deg, rgba(124,58,237,0.12), rgba(244,114,182,0.12)); }
.note-card:nth-child(6) { background: linear-gradient(135deg, rgba(245,158,11,0.1), rgba(74,144,217,0.12)); }
.note-card:nth-child(7) { background: linear-gradient(135deg, rgba(244,114,182,0.1), rgba(126,200,247,0.1)); }
.note-card:nth-child(8) { background: linear-gradient(135deg, rgba(74,144,217,0.15), rgba(245,158,11,0.08)); }
.note-card:nth-child(9) { background: linear-gradient(135deg, rgba(124,58,237,0.18), rgba(244,114,182,0.1)); }
.note-card:nth-child(10){ background: linear-gradient(135deg, rgba(74,144,217,0.12), rgba(124,58,237,0.15)); }

/* ────────────────────────────────────────
   TIMELINE
──────────────────────────────────────── */
#timeline {
  padding: 6rem 2rem;
  background: linear-gradient(180deg, #0a0a1a 0%, #0f0920 50%, #0a0a1a 100%);
}

.timeline-wrapper {
  max-width: 700px; margin: 0 auto;
  position: relative;
}
.timeline-wrapper::before {
  content: '';
  position: absolute; left: 50%; top: 0; bottom: 0;
  width: 2px;
  background: linear-gradient(to bottom, var(--purple), var(--blue), var(--purple));
  transform: translateX(-50%);
}

.tl-item {
  display: flex; align-items: center;
  margin-bottom: 3rem;
  animation: fadeInUp 0.8s ease both;
}
.tl-item:nth-child(even) { flex-direction: row-reverse; }

.tl-content {
  width: calc(50% - 2rem);
  background: var(--glass); border: 1px solid var(--glass-border);
  border-radius: 16px; padding: 1.5rem;
  backdrop-filter: blur(12px);
  transition: transform 0.3s ease;
}
.tl-content:hover { transform: scale(1.03); }

.tl-dot {
  width: 16px; height: 16px;
  border-radius: 50%; flex-shrink: 0;
  background: linear-gradient(135deg, var(--purple-light), var(--blue-light));
  box-shadow: 0 0 20px var(--purple-light);
  margin: 0 1rem; z-index: 1;
}

.tl-date {
  font-size: 0.7rem; letter-spacing: 0.2em; text-transform: uppercase;
  color: var(--blue-light); margin-bottom: 0.4rem;
}
.tl-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.2rem; font-weight: 600;
}
.tl-desc { font-size: 0.85rem; color: rgba(255,255,255,0.5); margin-top: 0.3rem; }
.tl-emoji { font-size: 1.5rem; margin-bottom: 0.5rem; }

/* ────────────────────────────────────────
   MARIGOLD GIFT
──────────────────────────────────────── */
#gift {
  padding: 6rem 2rem;
  background: #0a0a1a;
  text-align: center;
}

.flower-stage {
  max-width: 500px; margin: 0 auto;
  position: relative;
}

.marigold-svg {
  width: 200px; height: 200px;
  margin: 2rem auto;
  animation: flowerSpin 20s linear infinite, flowerFloat 4s ease-in-out infinite;
  filter: drop-shadow(0 0 30px rgba(245,158,11,0.5)) drop-shadow(0 0 60px rgba(245,158,11,0.3));
}
@keyframes flowerSpin { from{transform:rotate(0deg)} to{transform:rotate(360deg)} }
@keyframes flowerFloat {
  0%,100% { transform: rotate(0deg) translateY(0); }
  50% { transform: rotate(180deg) translateY(-15px); }
}

.gift-message {
  font-family: 'Dancing Script', cursive;
  font-size: clamp(1.3rem, 3vw, 1.8rem);
  color: rgba(255,255,255,0.8); line-height: 1.8;
  max-width: 500px; margin: 2rem auto;
}
.gift-message .highlight {
  color: var(--gold);
  text-shadow: 0 0 20px rgba(245,158,11,0.5);
}
.gift-message .highlight-b {
  color: var(--blue-light);
  text-shadow: 0 0 20px rgba(74,144,217,0.5);
}

/* ────────────────────────────────────────
   FUN FACTS - Astha's favourites
──────────────────────────────────────── */
#favorites {
  padding: 6rem 2rem;
  background: linear-gradient(180deg, #0a0a1a, #0d102a, #0a0a1a);
}

.fav-grid {
  max-width: 800px; margin: 0 auto;
  display: grid; grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.fav-card {
  background: var(--glass); border: 1px solid var(--glass-border);
  border-radius: 20px; padding: 2rem 1.5rem; text-align: center;
  backdrop-filter: blur(12px);
  transition: transform 0.3s, box-shadow 0.3s;
}
.fav-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 50px var(--shadow, rgba(74,144,217,0.3));
}
.fav-card.c-blue { --shadow: rgba(74,144,217,0.3); border-color: rgba(74,144,217,0.3); }
.fav-card.c-tulip { --shadow: rgba(244,114,182,0.3); border-color: rgba(244,114,182,0.3); }
.fav-card.c-num { --shadow: rgba(124,58,237,0.3); border-color: rgba(124,58,237,0.3); }

.fav-icon { font-size: 3rem; margin-bottom: 1rem; }
.fav-label { font-size: 0.7rem; letter-spacing: 0.25em; text-transform: uppercase; color: rgba(255,255,255,0.35); margin-bottom: 0.5rem; }
.fav-value {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.6rem; font-style: italic;
}
.fav-card.c-blue .fav-value { color: var(--blue-light); }
.fav-card.c-tulip .fav-value { color: var(--pink); }
.fav-card.c-num .fav-value { color: var(--purple-light); font-size: 3rem; }

/* ────────────────────────────────────────
   LETTER
──────────────────────────────────────── */
#letter {
  padding: 6rem 2rem;
  background: #0a0a1a;
}

.letter-wrapper {
  max-width: 680px; margin: 0 auto;
  background: linear-gradient(135deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 24px; padding: 3.5rem;
  backdrop-filter: blur(20px);
  position: relative; overflow: hidden;
}
.letter-wrapper::before {
  content: '';
  position: absolute; top: -2px; left: 30px; right: 30px; height: 2px;
  background: linear-gradient(90deg, transparent, var(--purple-light), var(--blue-light), transparent);
}

.letter-salutation {
  font-family: 'Dancing Script', cursive;
  font-size: 1.6rem; color: var(--blue-light);
  margin-bottom: 1.5rem;
}
.letter-body {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.1rem; line-height: 1.9;
  color: rgba(255,255,255,0.78);
  font-style: italic;
}
.letter-body p { margin-bottom: 1.2rem; }
.letter-sign {
  font-family: 'Dancing Script', cursive;
  font-size: 1.8rem; color: var(--purple-light);
  margin-top: 2rem; text-align: right;
}

.letter-tulips {
  position: absolute; top: 1rem; right: 1.5rem;
  font-size: 1.5rem; opacity: 0.5;
}

/* ────────────────────────────────────────
   FOOTER
──────────────────────────────────────── */
footer {
  padding: 4rem 2rem; text-align: center; position: relative; z-index: 2;
  background: #0a0a1a;
  border-top: 1px solid rgba(255,255,255,0.06);
}
.footer-hearts { font-size: 2rem; margin-bottom: 1rem; letter-spacing: 0.5rem; }
.footer-text { font-family: 'Dancing Script', cursive; font-size: 1.2rem; color: rgba(255,255,255,0.4); }
.footer-names { color: var(--purple-light); font-size: 1.5rem; }

/* ────────────────────────────────────────
   ANIMATIONS / UTILITIES
──────────────────────────────────────── */
@keyframes fadeInUp   { from{opacity:0;transform:translateY(30px)} to{opacity:1;transform:translateY(0)} }
@keyframes fadeInDown { from{opacity:0;transform:translateY(-20px)} to{opacity:1;transform:translateY(0)} }
@keyframes fadeIn     { from{opacity:0} to{opacity:1} }

.reveal {
  opacity: 0; transform: translateY(40px);
  transition: opacity 0.8s ease, transform 0.8s ease;
}
.reveal.visible { opacity: 1; transform: translateY(0); }

/* Glow text */
.glow-blue { text-shadow: 0 0 30px var(--blue-light), 0 0 60px rgba(74,144,217,0.4); }
.glow-purple { text-shadow: 0 0 30px var(--purple-light), 0 0 60px rgba(124,58,237,0.4); }

/* Responsive */
@media(max-width:600px){
  .fav-grid { grid-template-columns: 1fr 1fr; }
  .fav-card.c-num { grid-column: span 2; }
  .timeline-wrapper::before { left: 20px; }
  .tl-item, .tl-item:nth-child(even) { flex-direction: row; }
  .tl-dot { margin: 0 0.75rem 0 0; }
  .tl-content { width: calc(100% - 3rem); }
  .letter-wrapper { padding: 2rem; }
}
</style>
</head>
<body>

<div id="cursor"></div>
<div id="cursor-trail"></div>
<canvas id="stars-canvas"></canvas>

<!-- ════════════════════════════════════
     HERO
═════════════════════════════════════ -->
<section id="hero">
  <div class="hero-badge">✨ 5 Month Anniversary ✨</div>

  <h1 class="hero-title">
    <span class="name-r">Rishabh</span>
    <span class="heart"> ♡ </span>
    <span class="name-a">Astha</span>
  </h1>

  <p class="hero-sub">A love story worth every mile between us 💙💜</p>

  <div class="hero-months">5</div>
  <p class="hero-months-label">Months of pure magic</p>

  <div class="scroll-hint">
    <span>Scroll to explore</span>
    <div class="scroll-line"></div>
  </div>

  <div class="tulip-container">
    <span class="tulip">🌷</span><span class="tulip">🌷</span>
    <span class="tulip">🌷</span><span class="tulip">🌷</span>
    <span class="tulip">🌷</span><span class="tulip">🌷</span>
    <span class="tulip">🌷</span>
  </div>
</section>

<!-- ════════════════════════════════════
     DISTANCE TRACKER
═════════════════════════════════════ -->
<section id="distance">
  <h2 class="section-title reveal">Our <span>Distance</span></h2>
  <p class="section-sub reveal">Patiala ↔ Raigarh — Bridged by love</p>

  <div class="distance-map reveal">

    <div class="cities-row">
      <div class="city-card patiala">
        <div class="city-emoji">🌟</div>
        <div class="city-name">Patiala</div>
        <div class="city-person">Rishabh is here</div>
        <div class="city-state">Punjab</div>
      </div>

      <div class="distance-middle">
        <div class="distance-line"></div>
        <div class="distance-km">~1,700 km</div>
        <div class="distance-label">apart in body</div>
        <div style="font-size:0.7rem;color:rgba(255,255,255,0.25);letter-spacing:.1em;margin-top:.3rem">but 0 km apart in heart</div>
      </div>

      <div class="city-card raigarh">
        <div class="city-emoji">💫</div>
        <div class="city-name">Raigarh</div>
        <div class="city-person">Astha is here</div>
        <div class="city-state">Chhattisgarh</div>
      </div>
    </div>

    <hr style="border:none;border-top:1px solid rgba(255,255,255,0.08);margin:2rem 0;">

    <p style="text-align:center;font-family:'Dancing Script',cursive;font-size:1.2rem;color:rgba(255,255,255,0.5);margin-bottom:1.5rem">Time until we meet — June 5, 2026 💜</p>

    <div class="countdown-grid">
      <div class="count-card days">
        <div class="count-num" id="cnt-d">--</div>
        <div class="count-lbl">Days</div>
      </div>
      <div class="count-card hours">
        <div class="count-num" id="cnt-h">--</div>
        <div class="count-lbl">Hours</div>
      </div>
      <div class="count-card minutes">
        <div class="count-num" id="cnt-m">--</div>
        <div class="count-lbl">Minutes</div>
      </div>
      <div class="count-card seconds">
        <div class="count-num" id="cnt-s">--</div>
        <div class="count-lbl">Seconds</div>
      </div>
    </div>

    <div class="meet-soon-banner" id="meet-banner">
      🎉 Rishabh is SO excited to finally hold Astha's hand again! 🎉
    </div>
  </div>
</section>

<!-- ════════════════════════════════════
     LOVE NOTES
═════════════════════════════════════ -->
<section id="lovenotes">
  <h2 class="section-title reveal">Things <span>Rishu</span> Loves</h2>
  <p class="section-sub reveal">The little things that make everything perfect</p>

  <div class="notes-grid">
    <div class="note-card reveal">
      <div class="note-emoji">🥺</div>
      <div class="note-text">The way you call me <em>Rishu</em>. It hits different every single time.</div>
      <div class="note-num">01 / 10</div>
    </div>
    <div class="note-card reveal">
      <div class="note-emoji">🌙</div>
      <div class="note-text">Our late night video calls — falling asleep to your face is my favourite thing.</div>
      <div class="note-num">02 / 10</div>
    </div>
    <div class="note-card reveal">
      <div class="note-emoji">🔥</div>
      <div class="note-text">When you talk dirty... let's just say you have an extraordinary power over me 😅🫣</div>
      <div class="note-num">03 / 10</div>
    </div>
    <div class="note-card reveal">
      <div class="note-emoji">📚</div>
      <div class="note-text">My only favourite English teacher. You make words sound like poetry.</div>
      <div class="note-num">04 / 10</div>
    </div>
    <div class="note-card reveal">
      <div class="note-emoji">🎵</div>
      <div class="note-text">Your voice. I could listen to it on loop and never get tired.</div>
      <div class="note-num">05 / 10</div>
    </div>
    <div class="note-card reveal">
      <div class="note-emoji">😤</div>
      <div class="note-text">The expressions when you're mad at me — I can never, ever forget that day. Pure gold.</div>
      <div class="note-num">06 / 10</div>
    </div>
    <div class="note-card reveal">
      <div class="note-emoji">💃</div>
      <div class="note-text">I love your <em>kamar</em>, baby &lt;3 — you're absolutely everything.</div>
      <div class="note-num">07 / 10</div>
    </div>
    <div class="note-card reveal">
      <div class="note-emoji">👑</div>
      <div class="note-text"><em>Goddess.</em> That's all. That's the whole sentence. A literal goddess.</div>
      <div class="note-num">08 / 10</div>
    </div>
    <div class="note-card reveal">
      <div class="note-emoji">🪞</div>
      <div class="note-text">Also your boyfriend (he's <em>hawt</em> btw — don't @ me, facts are facts 💜)</div>
      <div class="note-num">09 / 10</div>
    </div>
    <div class="note-card reveal">
      <div class="note-emoji">🌸</div>
      <div class="note-text">Your smell. Sniff sniff sniff. I want to bottle it and keep it forever.</div>
      <div class="note-num">10 / 10</div>
    </div>
  </div>
</section>

<!-- ════════════════════════════════════
     TIMELINE
═════════════════════════════════════ -->
<section id="timeline">
  <h2 class="section-title reveal">Our <span>Story</span></h2>
  <p class="section-sub reveal">Every moment, etched in stars</p>

  <div class="timeline-wrapper">
    <div class="tl-item reveal">
      <div class="tl-content">
        <div class="tl-emoji">💌</div>
        <div class="tl-date">25 October 2025</div>
        <div class="tl-title">The Proposal 💍</div>
        <div class="tl-desc">Rishabh said the three most important words and changed everything.</div>
      </div>
      <div class="tl-dot"></div>
      <div style="width:calc(50% - 2rem)"></div>
    </div>

    <div class="tl-item reveal">
      <div style="width:calc(50% - 2rem)"></div>
      <div class="tl-dot"></div>
      <div class="tl-content">
        <div class="tl-emoji">🌸</div>
        <div class="tl-date">October 2025 — Now</div>
        <div class="tl-title">Long Distance Love</div>
        <div class="tl-desc">1,700 km apart, but every call, every text, every moment — pure magic.</div>
      </div>
    </div>

    <div class="tl-item reveal">
      <div class="tl-content">
        <div class="tl-emoji">💐</div>
        <div class="tl-date">March 25, 2026</div>
        <div class="tl-title">5 Month Anniversary 🎉</div>
        <div class="tl-desc">Rishabh gave Astha marigolds and built her this entire website. That's love.</div>
      </div>
      <div class="tl-dot"></div>
      <div style="width:calc(50% - 2rem)"></div>
    </div>

    <div class="tl-item reveal">
      <div style="width:calc(50% - 2rem)"></div>
      <div class="tl-dot"></div>
      <div class="tl-content">
        <div class="tl-emoji">✈️</div>
        <div class="tl-date">5 June 2026</div>
        <div class="tl-title">We Finally Meet! 🥺💜</div>
        <div class="tl-desc">The most awaited day. Rishabh is counting down every second.</div>
      </div>
    </div>
  </div>
</section>

<!-- ════════════════════════════════════
     MARIGOLD GIFT
═════════════════════════════════════ -->
<section id="gift">
  <h2 class="section-title reveal">A <span>Gift</span> For You</h2>
  <p class="section-sub reveal">🌼 Marigold — the flower I gave you today 🌼</p>

  <div class="flower-stage reveal">
    <svg class="marigold-svg" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
      <!-- petals -->
      <g transform="translate(100,100)">
        <ellipse rx="12" ry="38" fill="#f59e0b" opacity="0.9" transform="rotate(0) translate(0,-42)"/>
        <ellipse rx="12" ry="38" fill="#f59e0b" opacity="0.85" transform="rotate(30) translate(0,-42)"/>
        <ellipse rx="12" ry="38" fill="#fbbf24" opacity="0.9" transform="rotate(60) translate(0,-42)"/>
        <ellipse rx="12" ry="38" fill="#f59e0b" opacity="0.85" transform="rotate(90) translate(0,-42)"/>
        <ellipse rx="12" ry="38" fill="#fbbf24" opacity="0.9" transform="rotate(120) translate(0,-42)"/>
        <ellipse rx="12" ry="38" fill="#f59e0b" opacity="0.85" transform="rotate(150) translate(0,-42)"/>
        <ellipse rx="12" ry="38" fill="#fbbf24" opacity="0.9" transform="rotate(180) translate(0,-42)"/>
        <ellipse rx="12" ry="38" fill="#f59e0b" opacity="0.85" transform="rotate(210) translate(0,-42)"/>
        <ellipse rx="12" ry="38" fill="#fbbf24" opacity="0.9" transform="rotate(240) translate(0,-42)"/>
        <ellipse rx="12" ry="38" fill="#f59e0b" opacity="0.85" transform="rotate(270) translate(0,-42)"/>
        <ellipse rx="12" ry="38" fill="#fbbf24" opacity="0.9" transform="rotate(300) translate(0,-42)"/>
        <ellipse rx="12" ry="38" fill="#f59e0b" opacity="0.85" transform="rotate(330) translate(0,-42)"/>
        <!-- inner layer -->
        <ellipse rx="9" ry="28" fill="#fcd34d" opacity="0.95" transform="rotate(15) translate(0,-30)"/>
        <ellipse rx="9" ry="28" fill="#fcd34d" opacity="0.95" transform="rotate(75) translate(0,-30)"/>
        <ellipse rx="9" ry="28" fill="#fcd34d" opacity="0.95" transform="rotate(135) translate(0,-30)"/>
        <ellipse rx="9" ry="28" fill="#fcd34d" opacity="0.95" transform="rotate(195) translate(0,-30)"/>
        <ellipse rx="9" ry="28" fill="#fcd34d" opacity="0.95" transform="rotate(255) translate(0,-30)"/>
        <ellipse rx="9" ry="28" fill="#fcd34d" opacity="0.95" transform="rotate(315) translate(0,-30)"/>
        <!-- centre -->
        <circle r="20" fill="#92400e"/>
        <circle r="14" fill="#78350f"/>
        <circle r="7"  fill="#451a03"/>
      </g>
    </svg>

    <div class="gift-message">
      I gave you a <span class="highlight">marigold</span> today, Astha. 🌼<br>
      It's not a tulip (your favourite 🌷), I know —<br>
      but it blooms as bright as <span class="highlight-b">my love for you</span>.<br>
      <br>
      <em>Happy 5 months, baby.</em> 💜
    </div>
  </div>
</section>

<!-- ════════════════════════════════════
     ASTHA'S FAVOURITES
═════════════════════════════════════ -->
<section id="favorites">
  <h2 class="section-title reveal">Astha's <span>Favourites</span></h2>
  <p class="section-sub reveal">The little things that make her, her ✨</p>

  <div class="fav-grid reveal" style="max-width:700px;margin:0 auto;">
    <div class="fav-card c-blue">
      <div class="fav-icon">💙</div>
      <div class="fav-label">Favourite Color</div>
      <div class="fav-value">Blue</div>
    </div>
    <div class="fav-card c-tulip">
      <div class="fav-icon">🌷</div>
      <div class="fav-label">Favourite Flower</div>
      <div class="fav-value">Tulip</div>
    </div>
    <div class="fav-card c-num">
      <div class="fav-icon">✨</div>
      <div class="fav-label">Favourite Number</div>
      <div class="fav-value">6</div>
    </div>
  </div>
</section>

<!-- ════════════════════════════════════
     LETTER
═════════════════════════════════════ -->
<section id="letter">
  <h2 class="section-title reveal">A <span>Letter</span> From Rishu</h2>
  <p class="section-sub reveal">Written with a full heart 💜</p>

  <div class="letter-wrapper reveal">
    <div class="letter-tulips">🌷🌷🌷</div>
    <div class="letter-salutation">My dearest Astha,</div>
    <div class="letter-body">
      <p>Five months ago, you said yes, and my entire world shifted on its axis. What started as something beautiful has grown into the most precious thing in my life.</p>
      <p>1,700 kilometres separate us. That's a lot of missed hugs, a lot of goodnight kisses sent over text, a lot of nights where the only thing I want is to be next to you. But somehow, those late-night calls and your voice make the distance feel like nothing.</p>
      <p>I love the way you call me <em>Rishu</em> — even typing that makes me smile. I love how you're my English teacher, my best friend, my goddess, and somehow, you also chose me. The luckiest man alive? That's me.</p>
      <p>June 5th, 2026 — I'm counting down every single second. Every day that passes is one day closer to finally standing in front of you, and I promise I'll make every moment worth the wait.</p>
      <p>Here's to five months of love, late-night calls, and a future full of tulips 🌷 and marigolds 🌼. You're my favourite adventure, Astha.</p>
    </div>
    <div class="letter-sign">Forever yours,<br>Rishu 💜</div>
  </div>
</section>

<!-- ════════════════════════════════════
     FOOTER
═════════════════════════════════════ -->
<footer>
  <div class="footer-hearts">💜 💙 🌷 💜 💙</div>
  <div class="footer-text">Made with all the love in the world for</div>
  <div class="footer-names footer-text">Rishabh &amp; Astha</div>
  <div class="footer-text" style="margin-top:0.5rem;font-size:0.9rem">25 Oct 2025 → forever 🥂</div>
</footer>

<!-- ════════════════════════════════════
     SCRIPTS
═════════════════════════════════════ -->
<script>
/* ── Custom Cursor ── */
const cur = document.getElementById('cursor');
const trail = document.getElementById('cursor-trail');
document.addEventListener('mousemove', e => {
  cur.style.left = e.clientX + 'px';
  cur.style.top  = e.clientY + 'px';
  setTimeout(() => {
    trail.style.left = e.clientX + 'px';
    trail.style.top  = e.clientY + 'px';
  }, 80);
});

/* ── Stars Canvas ── */
const canvas = document.getElementById('stars-canvas');
const ctx = canvas.getContext('2d');
let stars = [];

function resizeCanvas() {
  canvas.width  = window.innerWidth;
  canvas.height = window.innerHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

function initStars() {
  stars = [];
  for (let i = 0; i < 200; i++) {
    stars.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      r: Math.random() * 1.5 + 0.3,
      o: Math.random(),
      s: Math.random() * 0.015 + 0.003,
      d: Math.random() > 0.5 ? 1 : -1
    });
  }
}
initStars();

function drawStars() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  stars.forEach(s => {
    s.o += s.s * s.d;
    if (s.o > 1 || s.o < 0.1) s.d *= -1;
    ctx.beginPath();
    ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
    const color = Math.random() > 0.5 ? '126,200,247' : '167,139,250';
    ctx.fillStyle = `rgba(${color},${s.o})`;
    ctx.fill();
  });
  requestAnimationFrame(drawStars);
}
drawStars();

/* ── Floating Particles ── */
const COLORS = ['#7c3aed','#4a90d9','#f472b6','#a78bfa','#7ec8f7','#f59e0b'];
function spawnParticle() {
  const p = document.createElement('div');
  p.className = 'particle';
  const size = Math.random() * 8 + 3;
  const color = COLORS[Math.floor(Math.random() * COLORS.length)];
  p.style.cssText = `
    width:${size}px;height:${size}px;
    left:${Math.random()*100}vw;
    background:${color};
    box-shadow:0 0 ${size*2}px ${color};
    animation-duration:${Math.random()*10+8}s;
    animation-delay:${Math.random()*5}s;
  `;
  document.body.appendChild(p);
  setTimeout(() => p.remove(), 20000);
}
setInterval(spawnParticle, 600);

/* ── Countdown ── */
function updateCountdown() {
  const target = new Date('2026-06-05T00:00:00');
  const now    = new Date();
  const diff   = target - now;
  if (diff <= 0) {
    document.getElementById('meet-banner').textContent = '🎉 THE DAY IS HERE! RISHABH MEETS ASTHA! 🎉';
    return;
  }
  const d = Math.floor(diff / 86400000);
  const h = Math.floor((diff % 86400000) / 3600000);
  const m = Math.floor((diff % 3600000)  / 60000);
  const s = Math.floor((diff % 60000)    / 1000);
  document.getElementById('cnt-d').textContent = d;
  document.getElementById('cnt-h').textContent = String(h).padStart(2,'0');
  document.getElementById('cnt-m').textContent = String(m).padStart(2,'0');
  document.getElementById('cnt-s').textContent = String(s).padStart(2,'0');
}
updateCountdown();
setInterval(updateCountdown, 1000);

/* ── Scroll Reveal ── */
const reveals = document.querySelectorAll('.reveal');
const io = new IntersectionObserver(entries => {
  entries.forEach((e, i) => {
    if (e.isIntersecting) {
      setTimeout(() => e.target.classList.add('visible'), i * 80);
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.1 });
reveals.forEach(r => io.observe(r));

/* ── Heart click sparkle ── */
document.addEventListener('click', e => {
  for (let i = 0; i < 6; i++) {
    const heart = document.createElement('div');
    heart.textContent = ['💙','💜','🌷','✨','💫','🌸'][Math.floor(Math.random()*6)];
    heart.style.cssText = `
      position:fixed;left:${e.clientX}px;top:${e.clientY}px;
      font-size:${Math.random()*16+10}px;
      pointer-events:none;z-index:9997;
      animation:clickHeart 0.9s ease forwards;
      --dx:${(Math.random()-0.5)*120}px;
      --dy:${-(Math.random()*80+40)}px;
    `;
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 900);
  }
});

const style = document.createElement('style');
style.textContent = `
  @keyframes clickHeart {
    0%   { opacity:1; transform:translate(0,0) scale(1); }
    100% { opacity:0; transform:translate(var(--dx),var(--dy)) scale(0.5); }
  }
`;
document.head.appendChild(style);
</script>
</body>
</html>"""


try:
    import streamlit as st
    import streamlit.components.v1 as components
    STREAMLIT = True
except ImportError:
    STREAMLIT = False


def run_streamlit():
    st.set_page_config(
        page_title="Rishabh ♡ Astha — 5 Months",
        page_icon="💜",
        layout="wide",
    )
    # hide streamlit chrome for a clean full-page feel
    st.markdown("""
        <style>
        #MainMenu, header, footer { visibility: hidden; }
        .block-container { padding: 0 !important; max-width: 100% !important; }
        </style>
    """, unsafe_allow_html=True)
    components.html(HTML, height=6000, scrolling=True)


def run_http():
    """Fallback: plain HTTP server with automatic port selection."""
    import http.server, socketserver, webbrowser, threading

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML.encode("utf-8"))
        def log_message(self, *a): pass

    for port in range(8080, 8100):
        try:
            server = socketserver.TCPServer(("", port), Handler)
            server.allow_reuse_address = True
            break
        except OSError:
            continue
    else:
        print("❌ Could not find a free port between 8080-8099.")
        return

    print(f"\n💜 Opening at http://localhost:{port}  — press Ctrl+C to stop\n")
    threading.Thread(target=lambda: (time.sleep(1.2), webbrowser.open(f"http://localhost:{port}")), daemon=True).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n💜 Server stopped. Love never does. 💙")


if __name__ == "__main__":
    if STREAMLIT:
        run_streamlit()
    else:
        run_http()
