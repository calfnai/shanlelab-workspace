const $=s=>document.querySelector(s), data=window.WORKSPACE;
const escapeHTML=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const base='https://aion.welovetiktok.com';
let shown=[],selected=0;
const chatUrl=id=>base+'/#/conversation/'+encodeURIComponent(id);
const conversationLink=p=>`<a class="primary" href="${escapeHTML(chatUrl(p.conversation))}" target="_blank" rel="noopener">在网页中继续对话 ↗</a>`;
$('#date').textContent=data.updated.replaceAll('-','.');
const navItems=ps=>ps.map(p=>`<a href="#${p.id}" data-id="${p.id}"><small>↗</small>${p.title}</a>`).join('');
$('#navigation').innerHTML='<a href="#home" data-id="home"><small>⌂</small>全部项目</a><div class="side-label">近期推进</div>'+navItems(data.projects.filter(p=>p.lifecycle!=='ongoing'))+'<div class="side-label">长期项目</div>'+navItems(data.projects.filter(p=>p.lifecycle==='ongoing'));

const thumb=(item)=>`<img src="${encodeURI(item.thumb)}" alt="${escapeHTML(item.label)}" loading="lazy">`;
function toast(message){$('#toast').textContent=message;$('#toast').classList.add('show');setTimeout(()=>$('#toast').classList.remove('show'),3000);}
function card(p){return `<article class="card"><a class="cover" href="#${p.id}">${thumb(p.items[0])}<span class="cover-tag">${p.items[0].status}</span></a><div class="card-body"><div class="card-en">${p.en}</div><a class="card-title" href="#${p.id}"><h2>${p.title}</h2><span class="arrow">↗</span></a><p>${p.description}</p><div class="card-meta"><span>${p.items.length} 张图稿${p.links.some(x=>x.kind==='3d')?' · 可旋转 3D':''}</span><span>进入项目 →</span></div></div></article>`;}
function projectSections(ps){
 const recent=ps.filter(p=>p.lifecycle!=='ongoing'),ongoing=ps.filter(p=>p.lifecycle==='ongoing');
 return (recent.length?`<div class="toolbar"><h2>近期推进 <small>RECENT WORK</small></h2></div><section class="cards">${recent.map(card).join('')}</section>`:'')+(ongoing.length?`<div class="toolbar"><h2>长期项目 <small>ONGOING</small></h2></div><p>持续维护，不按近期可完结任务排列。</p><section class="cards">${ongoing.map(card).join('')}</section>`:'')||'<p class="empty">没有找到匹配的项目。</p>';
}
function projectScope(p){
 return (p.currentFocus?`<section><h2>${p.lifecycle==='ongoing'?'持续维护':'当前推进'}</h2><div class="notice">${escapeHTML(p.currentFocus)}</div></section>`:'')+(p.cancelledScope?`<div class="notice"><b>已取消的范围</b><br>${escapeHTML(p.cancelledScope)}</div>`:'')+(p.workstreams?`<section><h2>同一项目的不同层面</h2><div class="cards">${p.workstreams.map(w=>`<article class="card"><div class="card-body"><h3>${escapeHTML(w.title)}</h3><p>${escapeHTML(w.summary)}</p></div></article>`).join('')}</div></section>`:'');
}
function art(item,i){return `<article class="art"><button data-image="${i}" aria-label="放大 ${escapeHTML(item.label)}">${thumb(item)}</button><div class="art-body"><span class="art-status">${escapeHTML(item.status)}</span><h3>${escapeHTML(item.label)}</h3>${item.note?`<p>${escapeHTML(item.note)}</p>`:''}</div></article>`;}
function projectProgress(p){
 const r=p.progress;if(!r)return '';
 const visuals=(r.visualGroups||[]).map(group=>`<section class="progress-visual-group"><h3>${escapeHTML(group.title)}</h3><p>${escapeHTML(group.note||'')}</p><div class="progress-visual-grid">${group.files.map(file=>{const i=p.items.findIndex(item=>item.file===file),item=p.items[i]||(p.reviewArchive||[]).find(item=>item.file===file);if(!item)return '';const picture=`<img src="${encodeURI(item.file)}" alt="${escapeHTML(item.label)}" loading="lazy">`;return `<figure>${i>=0?`<button data-image="${i}" aria-label="放大 ${escapeHTML(item.label)}">${picture}</button>`:`<a href="${encodeURI(item.file)}" target="_blank" rel="noopener">${picture}</a>`}<figcaption><b>${escapeHTML(item.label)}</b><p><strong>${escapeHTML(item.status)}</strong></p><p>${escapeHTML(item.note||'')}</p></figcaption></figure>`;}).join('')}</div></section>`).join('');
 const cards=rows=>`<div class="cards">${rows.map(x=>`<article class="card"><div class="card-body"><h3>${escapeHTML(x.title)}</h3>${x.quote?`<blockquote>“${escapeHTML(x.quote)}”</blockquote>`:''}<p>${escapeHTML(x.detail)}</p>${x.conversation?`<a href="${escapeHTML(chatUrl(x.conversation))}" target="_blank" rel="noopener">查看原对话 ↗</a>`:''}</div></article>`).join('')}</div>`;
 return `<section class="project-progress"><h2>做到哪一步 · ${escapeHTML(r.updated)}</h2><p>${escapeHTML(r.summary)}</p>${visuals}<h2>下次从这里继续</h2>${cards(r.next)}<h2>关键沟通与决定</h2>${cards(r.decisions)}<h2>阶段记录与其他版本</h2>${cards(r.history)}<div class="actions">${r.sources.map(s=>`<a href="${escapeHTML(chatUrl(s.conversation))}" target="_blank" rel="noopener">${escapeHTML(s.label)} ↗</a>`).join('')}</div></section>`;
}
function milestone(p,home=false){
 const m=p?.milestone;if(!m)return '';
 const email=m.email?`<div class="email-stage"><small>阶段成果 / ${m.email.date}</small><h3>${m.email.title}</h3><p>${m.email.summary}</p><div class="actions"><a href="${m.email.href}" target="_blank" rel="noopener">查看已发送正文 ↗</a>${m.email.latestHref?`<a href="${m.email.latestHref}" target="_blank" rel="noopener">${m.email.latestTitle||'后续完整邮件草稿'} ↗</a>`:''}</div></div>`:'';
 return `<section class="milestone"><div class="milestone-image">${home?`<a href="#${p.id}">${thumb(p.items[0])}</a>`:`<button data-image="0" aria-label="放大${escapeHTML(m.title)}">${thumb(p.items[0])}</button>`}<span>${m.status} · ${m.date}</span></div><div class="milestone-copy"><div class="eyebrow">CURRENT MILESTONE / ${p.title}</div><h2>${m.title}</h2><p>${m.summary}</p><div class="milestone-state"><b>✓ ${m.status}</b><span>${m.approvalNote||(p.id==='mlbb-gift'?'合作方书面批准状态另行核对':'')}</span></div>${email}${home?`<a class="action" href="#${p.id}">进入项目继续 →</a>`:m.next?`<p class="next-step">${m.next}</p>`:''}</div></section>`;
}

function render(){
 const id=location.hash.slice(1)||'home',p=data.projects.find(p=>p.id===id);
 document.querySelectorAll('nav a').forEach(a=>a.classList.toggle('active',a.dataset.id===(p?p.id:'home')));
 if(!p){document.title='SHANLE 共享工作区 · SHANLE LAB';$('#content').innerHTML=`<section class="hero"><div><div class="eyebrow">A PLACE TO PICK UP WHERE YOU LEFT OFF</div><h1>SHANLE 的工作，<br><em>从这里继续。</em></h1><p>找到成果，回看版本，接着把事情做下去。</p></div><div class="hero-note"><div class="stats"><div><strong>${String(data.projects.length).padStart(2,'0')}</strong><span>个项目方向</span></div><div><strong>${data.projects.reduce((n,p)=>n+p.items.length,0)}</strong><span>张真实图稿</span></div><div><strong>${String(data.projects.reduce((n,p)=>n+p.links.filter(l=>l.kind==='3d').length,0)).padStart(2,'0')}</strong><span>个可旋转演示</span></div></div><p>多个项目与对话共用这一工作区。各自更新成果、版本与接续入口，最近确认的版本优先展示。<br><a href="workspace-guide.html">如何在其他对话中更新此工作区 ↗</a></p></div></section>${data.projects.filter(p=>p.milestone).sort((a,b)=>b.milestone.date.localeCompare(a.milestone.date)).map(p=>milestone(p,true)).join('')}<div class="toolbar"><h2>项目索引 <small>SHANLE PROJECTS</small></h2><input type="search" id="search" placeholder="搜索项目、版本、图稿…" aria-label="搜索项目与图稿"></div><div id="results">${projectSections(data.projects)}</div>`;
 $('#search').oninput=e=>{const q=e.target.value.trim().toLowerCase(),ps=data.projects.filter(p=>(p.title+p.description+p.items.map(i=>i.label).join('')).toLowerCase().includes(q));$('#results').innerHTML=projectSections(ps);};
 }else{
 document.title=p.title+' · SHANLE 共享工作区';shown=p.items;
 if(p.id==='overseas-catalogs'&&p.workbench){renderOverseas(p);return;}
 if(p.comparison){renderNiko(p);return;}
 $('#content').innerHTML=`<section class="work-title"><a href="#home" class="back">← 返回全部项目</a><div class="eyebrow" style="margin-top:25px">${p.en}</div><h1>${p.title}</h1><p>${p.description}</p><div class="notice">${p.note}</div><div class="actions">${p.links.map(l=>`<a href="${encodeURI(l.href)}" target="_blank" rel="noopener" class="${l.kind==='3d'?'primary':''}">${l.label} ↗</a>`).join('')}${conversationLink(p)}<button id="copy-name">复制对话名称</button><button id="copy-chat">复制对话 ID</button><a href="${base}" target="_blank" rel="noopener">网页服务首页 ↗</a></div><p class="hint">对话：${escapeHTML(p.conversationName)} · 通过 AionUi 网页入口接续；需通过 Cloudflare Access 验证并登录。</p></section>${projectScope(p)}${milestone(p)}${projectProgress(p)}<div class="toolbar"><h2>${p.galleryLabel|| (p.lifecycle==='ongoing'?'阶段成果':p.milestone?'其他版本':'图稿与版本')} <small>${p.items.length-(p.milestone?1:0)} IMAGES</small></h2><input type="search" id="version-search" placeholder="筛选版本或关键词…" aria-label="筛选版本或关键词"></div><section class="gallery" id="gallery">${shown.map((item,i)=>p.milestone&&i===0?'':art(item,i)).join('')}</section>`;
 $('#version-search').oninput=e=>{const q=e.target.value.toLowerCase();$('#gallery').innerHTML=shown.map((item,i)=>(p.milestone&&i===0)||!(item.label+item.status+item.note).toLowerCase().includes(q)?'':art(item,i)).join('')||'<p class="empty">没有找到匹配的图稿。</p>';};
 $('#copy-name').onclick=async()=>{try{await navigator.clipboard.writeText(p.conversationName);toast('已复制：'+p.conversationName);}catch{toast(p.conversationName);}};$('#copy-chat').onclick=async()=>{try{await navigator.clipboard.writeText(p.conversation);toast('已复制对话 ID：'+p.conversation);}catch{toast('对话 ID：'+p.conversation);}};
 }
}
function showImage(i){if(!shown.length)return;selected=(i+shown.length)%shown.length;const item=shown[selected];$('#full-image').src=item.file;$('#full-image').alt=item.label;$('#caption').textContent=item.label+' · '+item.status;$('#position').textContent=`${selected+1} / ${shown.length}`;$('#original').href=item.file;if(!$('#lightbox').open)$('#lightbox').showModal();}
$('#content').onclick=e=>{const b=e.target.closest('[data-image]');if(b)showImage(Number(b.dataset.image));};
$('#close-image').onclick=()=>$('#lightbox').close();$('#previous').onclick=()=>showImage(selected-1);$('#next').onclick=()=>showImage(selected+1);
document.addEventListener('keydown',e=>{if($('#lightbox').open&&e.key==='ArrowLeft')showImage(selected-1);if($('#lightbox').open&&e.key==='ArrowRight')showImage(selected+1);});
window.addEventListener('hashchange',()=>{render();scrollTo(0,0);});render();
