
// mobile menu
const toggle=document.querySelector('.menu-toggle');
const links=document.getElementById('nav-links');
toggle?.addEventListener('click',()=>{
  const open=links.classList.toggle('open');
  toggle.setAttribute('aria-expanded',open);
});

// estimator (only if present)
const form=document.getElementById('estimate-form');
if(form){
  const $=s=>document.querySelector(s);
  function sumSelected(select){
    return [...select.selectedOptions].map(o=>+o.value).reduce((a,b)=>a+b,0);
  }
  function calc(){
    const living = +$('#living').value;
    const beds = sumSelected($('#bedrooms'));
    const dining = +$('#dining').value;
    const addons = [...document.querySelectorAll('.addons input:checked')].reduce((a,b)=>a+ +b.value,0);
    let total = living + beds + dining + addons;
    if ($('#flex')?.checked) total = Math.round(total * 1.2);
    $('#total').textContent = `$${(total||0).toLocaleString()}`;
    return total;
  }
  ['change','input'].forEach(evt => form.addEventListener(evt, calc));
  calc();
  document.getElementById('email-quote')?.addEventListener('click', ()=>{
    const t = calc();
    const body = encodeURIComponent(`Hi Amber-Modern,\n\nQuick estimate total: $${t}.\n\nDetails attached from the estimator.\n\nPlease contact me to finalize.`);
    location.href = `mailto:AmberModernDesign@gmail.com?subject=Amber-Modern Quote&body=${body}`;
  });
}

// lightbox (gallery pages)
const gal=document.getElementById('gal');
if(gal){
  const lb=document.createElement('div');
  lb.className='lightbox';
  lb.innerHTML=`<button class="close" aria-label="Close">Close ✕</button>
                <button class="prev" aria-label="Previous">‹</button>
                <img alt="Gallery image" />
                <button class="next" aria-label="Next">›</button>`;
  document.body.appendChild(lb);
  const items=[...gal.querySelectorAll('a')];
  const img=lb.querySelector('img'); const prev=lb.querySelector('.prev'); const next=lb.querySelector('.next'); const close=lb.querySelector('.close');
  let i=0;
  function open(k){i=k; img.src=items[i].href; lb.classList.add('open');}
  function move(d){i=(i+d+items.length)%items.length; img.src=items[i].href;}
  items.forEach((a,idx)=>a.addEventListener('click',e=>{e.preventDefault(); open(idx);}));
  close.addEventListener('click',()=>lb.classList.remove('open'));
  prev.addEventListener('click',()=>move(-1)); next.addEventListener('click',()=>move(1));
  lb.addEventListener('click',e=>{ if(e.target===lb) lb.classList.remove('open'); });
  document.addEventListener('keydown',e=>{
    if(!lb.classList.contains('open')) return;
    if(e.key==='Escape') lb.classList.remove('open');
    if(e.key==='ArrowLeft') move(-1);
    if(e.key==='ArrowRight') move(1);
  });
}

// ===== Menu behavior fixes (v6) =====
(function(){
  const toggle=document.querySelector('.menu-toggle');
  const links=document.getElementById('nav-links');
  if(toggle && links){
    // Close menu when any link is clicked
    links.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
      links.classList.remove('open');
      toggle.setAttribute('aria-expanded','false');
    }));
    // Close drawer when resizing to desktop
    let lastW = window.innerWidth;
    window.addEventListener('resize', ()=>{
      const w = window.innerWidth;
      if(w>=1001 && links.classList.contains('open')){
        links.classList.remove('open');
        toggle.setAttribute('aria-expanded','false');
      }
      lastW = w;
    });
  }
})();
