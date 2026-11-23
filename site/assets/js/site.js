(function(){
  const html=document.documentElement;
  html.classList.remove('no-js');
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const hasG=typeof gsap!=='undefined';
  if(hasG) gsap.registerPlugin(ScrollTrigger);

  /* smooth scroll */
  let lenis=null;
  if(!reduce && typeof Lenis!=='undefined'){
    lenis=new Lenis({lerp:.1,smoothWheel:true});
    lenis.on('scroll',()=>hasG&&ScrollTrigger.update());
    gsap.ticker.add(t=>lenis.raf(t*1000));
    gsap.ticker.lagSmoothing(0);
  }

  /* nav */
  const nav=document.querySelector('.nav');
  let lastY=0;
  const onScroll=()=>{
    const y=window.scrollY;
    nav.classList.toggle('scrolled',y>20||document.body.dataset.page!=='home');
    const megaOpen=document.querySelector('.mega.open');
    nav.classList.toggle('hide',y>lastY&&y>400&&!megaOpen&&!html.classList.contains('menu-open'));
    lastY=y;
  };
  addEventListener('scroll',onScroll,{passive:true});onScroll();

  const mega=document.querySelector('.mega');
  const megaLi=document.querySelector('.has-mega');
  if(mega&&megaLi){
    let t,openedAt=0;
    const open=()=>{clearTimeout(t);if(!mega.classList.contains('open'))openedAt=Date.now();mega.classList.add('open');megaLi.classList.add('open')};
    const close=()=>{t=setTimeout(()=>{mega.classList.remove('open');megaLi.classList.remove('open')},160)};
    megaLi.addEventListener('mouseenter',open);megaLi.addEventListener('mouseleave',close);
    mega.addEventListener('mouseenter',open);mega.addEventListener('mouseleave',close);
    megaLi.querySelector('button').addEventListener('click',()=>(mega.classList.contains('open')&&Date.now()-openedAt>400)?(mega.classList.remove('open'),megaLi.classList.remove('open')):open());
    addEventListener('keydown',e=>{if(e.key==='Escape'){mega.classList.remove('open');megaLi.classList.remove('open')}});
  }
  const burger=document.querySelector('.burger');
  burger&&burger.addEventListener('click',()=>{
    html.classList.toggle('menu-open');
    const o=html.classList.contains('menu-open');
    burger.setAttribute('aria-expanded',o);
    lenis&&(o?lenis.stop():lenis.start());
  });
  document.querySelectorAll('.mnav a').forEach(a=>a.addEventListener('click',()=>html.classList.remove('menu-open')));

  /* forms */
  document.querySelectorAll('form.form').forEach(f=>f.addEventListener('submit',e=>{
    e.preventDefault();f.querySelector('.ok').style.display='block';f.querySelector('.btn').style.display='none';
  }));

  /* monitor tabs */
  const tabs=[...document.querySelectorAll('.screen-bar .tabs button')];
  const shots=[...document.querySelectorAll('.screen-view img')];
  if(tabs.length){
    let i=0,timer;
    const set=n=>{i=n;tabs.forEach((b,k)=>b.classList.toggle('on',k===n));shots.forEach((s,k)=>s.classList.toggle('on',k===n))};
    const auto=()=>{clearInterval(timer);timer=setInterval(()=>set((i+1)%tabs.length),3800)};
    tabs.forEach((b,k)=>b.addEventListener('click',()=>{set(k);auto()}));
    set(0);auto();
  }

  if(!hasG||reduce){
    document.querySelectorAll('.rv').forEach(e=>{e.style.opacity=1;e.style.transform='none'});
    document.querySelectorAll('.pump').forEach((p,k)=>p.style.opacity=k===0?1:0);
    const l=document.querySelector('.loader');l&&l.remove();
    return;
  }

  /* loader + hero intro */
  const loader=document.querySelector('.loader');
  const intro=gsap.timeline({paused:true});
  const heroLines=document.querySelectorAll('.hero h1 .line>span, .phero h1 .line>span');
  if(heroLines.length){
    gsap.set(heroLines,{yPercent:110});
    intro.to(heroLines,{yPercent:0,duration:1.15,ease:'expo.out',stagger:.09});
  }
  const heroFade=document.querySelectorAll('.hero-in');
  if(heroFade.length){gsap.set(heroFade,{opacity:0,y:24});intro.to(heroFade,{opacity:1,y:0,duration:1,ease:'expo.out',stagger:.07},'-=.85')}
  if(loader&&!sessionStorage.getItem('ksi-l')){
    try{sessionStorage.setItem('ksi-l','1')}catch(e){}
    gsap.timeline()
      .to('.loader-bar i',{scaleX:1,duration:.9,ease:'power2.inOut'})
      .to('.loader-in',{opacity:0,y:-16,duration:.35,ease:'power2.in'})
      .to(loader,{clipPath:'inset(0 0 100% 0)',duration:.8,ease:'expo.inOut'},'-=.05')
      .add(()=>{loader.remove();intro.play()},'-=.45');
  }else{loader&&loader.remove();intro.play()}

  /* hero pump carousel */
  const pumps=[...document.querySelectorAll('.hero .pump')];
  const caps=pumps.map(p=>({t:p.dataset.title,d:p.dataset.desc}));
  const capT=document.querySelector('.stage-cap h4'),capD=document.querySelector('.stage-cap p'),capN=document.querySelector('.stage-cap .count');
  if(pumps.length){
    let cur=0;
    gsap.set(pumps,{opacity:0,x:60,scale:.94});
    gsap.to(pumps[0],{opacity:1,x:0,scale:1,duration:1.4,ease:'expo.out',delay:loader?1.4:.2});
    const go=()=>{
      const prev=pumps[cur];cur=(cur+1)%pumps.length;const nx=pumps[cur];
      gsap.to(prev,{opacity:0,x:-70,scale:.96,duration:.8,ease:'power3.in'});
      gsap.fromTo(nx,{opacity:0,x:80,scale:.94},{opacity:1,x:0,scale:1,duration:1.2,ease:'expo.out',delay:.55});
      gsap.to([capT,capD],{opacity:0,y:-8,duration:.35,onComplete:()=>{capT.textContent=caps[cur].t;capD.textContent=caps[cur].d;capN.textContent=String(cur+1).padStart(2,'0')+' / '+String(pumps.length).padStart(2,'0');gsap.to([capT,capD],{opacity:1,y:0,duration:.6,ease:'expo.out',stagger:.05})}});
    };
    setInterval(()=>{if(!document.hidden)go()},3600);
    gsap.to('.stage-ring',{rotate:360,duration:60,repeat:-1,ease:'none'});
    gsap.to('.stage',{yPercent:-12,ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'bottom top',scrub:true}});
  }

  /* reveals */
  ScrollTrigger.batch('.rv',{start:'top 88%',once:true,onEnter:b=>gsap.to(b,{opacity:1,y:0,duration:1.1,ease:'expo.out',stagger:.08})});

  /* parallax media */
  document.querySelectorAll('[data-par]').forEach(el=>{
    gsap.fromTo(el,{yPercent:-(+el.dataset.par)},{yPercent:+el.dataset.par,ease:'none',scrollTrigger:{trigger:el.parentElement,start:'top bottom',end:'bottom top',scrub:true}});
  });

  /* word reveal */
  document.querySelectorAll('.reveal-words').forEach(el=>{
    const words=el.textContent.trim().split(/\s+/);
    el.innerHTML=words.map(w=>'<span class="w">'+w+'</span>').join(' ');
    gsap.to(el.querySelectorAll('.w'),{color:'#08131f',stagger:.1,ease:'none',scrollTrigger:{trigger:el,start:'top 80%',end:'bottom 45%',scrub:true}});
  });

  /* lineup horizontal */
  const mm=gsap.matchMedia();
  mm.add('(min-width:681px)',()=>{
    const track=document.querySelector('.track');
    if(!track)return;
    const dist=()=>track.scrollWidth-innerWidth;
    gsap.to(track,{x:()=>-dist(),ease:'none',scrollTrigger:{trigger:'.track-wrap',start:'top top',end:()=>'+='+dist(),pin:true,scrub:.6,invalidateOnRefresh:true}});
    track.querySelectorAll('.pcard img').forEach(img=>{
      gsap.fromTo(img,{rotate:-4,scale:.9},{rotate:3,scale:1.04,ease:'none',scrollTrigger:{trigger:'.track-wrap',start:'top top',end:()=>'+='+dist(),scrub:true}});
    });
  });

  /* zagon list */
  const zl=[...document.querySelectorAll('.zlist a')],zi=[...document.querySelectorAll('.zvis img')],zp=document.querySelector('.zprog i');
  if(zl.length){
    const set=n=>{zl.forEach((a,k)=>a.classList.toggle('on',k===n));zi.forEach((m,k)=>m.classList.toggle('on',k===n));zp&&gsap.to(zp,{width:((n+1)/zl.length*100)+'%',duration:.6,ease:'expo.out'})};
    zl.forEach((a,k)=>{
      a.addEventListener('mouseenter',()=>set(k));
      ScrollTrigger.create({trigger:a,start:'top 60%',end:'bottom 60%',onToggle:s=>s.isActive&&set(k)});
    });
    set(0);
  }

  /* coupling alignment */
  const cp=document.querySelector('.coupling');
  if(cp){
    const tl=gsap.timeline({scrollTrigger:{trigger:cp,start:'top 75%',end:'bottom 40%',scrub:.8}});
    tl.fromTo('#half-r',{y:-26,rotate:-4,transformOrigin:'50% 50%'},{y:0,rotate:0,ease:'power2.out'},0)
      .fromTo('#needle',{rotate:-58,transformOrigin:'100px 100px'},{rotate:0,ease:'power2.out'},0)
      .fromTo('#readout',{textContent:0.48},{textContent:0,snap:{textContent:.01},ease:'power2.out'},0)
      .fromTo('#ok',{opacity:0},{opacity:1,duration:.15},.85);
    gsap.to('#shaft-spin',{rotate:360,transformOrigin:'50% 50%',duration:3,repeat:-1,ease:'none'});
  }

  /* steps icons draw */
  document.querySelectorAll('.step-ico path, .card-art path, .card-art circle').forEach(p=>{
    const len=p.getTotalLength?p.getTotalLength():0;if(!len)return;
    gsap.fromTo(p,{strokeDasharray:len,strokeDashoffset:len},{strokeDashoffset:0,duration:1.6,ease:'power2.out',scrollTrigger:{trigger:p.closest('.step,.card'),start:'top 85%',once:true}});
  });
  gsap.to('.impeller',{rotate:360,transformOrigin:'50% 50%',duration:6,repeat:-1,ease:'none'});

  /* marquee */
  const mq=document.querySelector('.marq');
  if(mq){
    mq.innerHTML+=mq.innerHTML;
    const w=()=>mq.scrollWidth/2;
    const loop=gsap.to(mq,{x:()=>-w(),duration:40,repeat:-1,ease:'none'});
    ScrollTrigger.create({trigger:'.values',start:'top bottom',end:'bottom top',onUpdate:s=>{gsap.to(loop,{timeScale:1+Math.min(Math.abs(s.getVelocity())/400,5)*(s.direction),duration:.2,overwrite:true});gsap.to(loop,{timeScale:1,duration:1.2,delay:.2})}});
  }

  /* CTA phone */
  const ph=document.querySelector('.cta .phone');
  ph&&gsap.fromTo(ph,{xPercent:12},{xPercent:-4,ease:'none',scrollTrigger:{trigger:'.cta',start:'top bottom',end:'bottom bottom',scrub:true}});
  gsap.utils.toArray('.wave-path').forEach((p,k)=>gsap.to(p,{x:-200,duration:6+k*2,repeat:-1,ease:'none'}));

  /* counters */
  document.querySelectorAll('[data-count]').forEach(el=>{
    const v=+el.dataset.count;
    gsap.fromTo(el,{textContent:0},{textContent:v,snap:{textContent:1},duration:1.6,ease:'power2.out',scrollTrigger:{trigger:el,start:'top 85%',once:true}});
  });

  addEventListener('load',()=>ScrollTrigger.refresh());
})();
