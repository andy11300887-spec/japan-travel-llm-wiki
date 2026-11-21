'use strict';
(function () {
  const slides = Array.from(document.querySelectorAll('.slide'));
  const dots = Array.from(document.querySelectorAll('.nav-dot'));
  const prev = document.getElementById('prev');
  const next = document.getElementById('next');
  const page = document.getElementById('page-now');
  const fill = document.getElementById('progress-fill');
  let current = 0;
  function show(i, updateHash = true) {
    if (!Number.isInteger(i)) return;
    current = Math.min(slides.length - 1, Math.max(0, i));
    slides.forEach((el, ix) => { el.classList.toggle('active', ix === current); el.setAttribute('aria-hidden', String(ix !== current)); });
    dots.forEach((el, ix) => { el.classList.toggle('active', ix === current); if(ix === current) el.setAttribute('aria-current','page'); else el.removeAttribute('aria-current'); });
    page.textContent = String(current + 1).padStart(2,'0');
    fill.style.width = `${(current + 1) / slides.length * 100}%`;
    prev.disabled = current === 0;
    next.disabled = current === slides.length - 1;
    const scroller = slides[current]; scroller.scrollTop = 0;
    if(updateHash && location.hash !== '#slide-' + (current + 1)) history.replaceState(null, '', '#slide-' + (current + 1));
  }
  prev.addEventListener('click', () => show(current - 1));
  next.addEventListener('click', () => show(current + 1));
  dots.forEach(d => d.addEventListener('click', () => show(Number(d.dataset.go))));
  document.addEventListener('keydown', e => {
    if (/^(input|textarea|select)$/i.test(document.activeElement.tagName)) return;
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    if (['ArrowRight','PageDown'].includes(e.key)) { e.preventDefault(); show(current+1); }
    if (['ArrowLeft','PageUp'].includes(e.key)) { e.preventDefault(); show(current-1); }
  });
  addEventListener('hashchange', () => {const m = location.hash.match(/^#slide-(\d+)$/); if(m) show(Number(m[1])-1,false);});
  const initialMatch = location.hash.match(/^#slide-(\d+)$/);
  show(initialMatch ? Number(initialMatch[1])-1 : 0, false);

  const budgetInputs = [...document.querySelectorAll('[data-budget]')];
  const preset = [35000,28000,12000,15000,6000,14000];
  const fmt = n => '¥' + n.toLocaleString('ja-JP');
  function recalc() {
    let total = 0;
    budgetInputs.forEach(inp => { const value = Number(inp.value); total += (Number.isFinite(value) && value > 0) ? Math.round(value) : 0; });
    document.getElementById('budget-total').textContent = fmt(total);
  }
  budgetInputs.forEach(el => el.addEventListener('input', recalc));
  document.getElementById('reset-budget').addEventListener('click', () => { budgetInputs.forEach((e,i) => e.value = preset[i]); recalc(); });
  recalc();

  const quiz = document.getElementById('mini-quiz');
  quiz.addEventListener('submit', e => {
    e.preventDefault();
    const answers = ['b','b','a'];
    let count = 0, missing = 0;
    answers.forEach((correct,i) => { const selected = quiz.querySelector(`input[name="q${i+1}"]:checked`); if(!selected) missing++; else if(selected.value === correct) count++; });
    document.getElementById('quiz-result').textContent = missing ? `請先完成全部3題（還有${missing}題）` : `答對 ${count} / 3 題。${count === 3 ? '太棒了，你掌握了基本原則！' : '可以回前面章節再複習一次。'}`;
  });
})();
