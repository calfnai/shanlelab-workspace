import * as T from './vendor/three.module.js';import{OrbitControls}from './vendor/OrbitControls.js';
const D=await(await fetch('./reach-data.json')).json(),V=document.querySelector('#viewport'),scene=new T.Scene();scene.background=new T.Color('#e9edf0');
const camera=new T.PerspectiveCamera(36,1,.02,50),renderer=new T.WebGLRenderer({antialias:true,preserveDrawingBuffer:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.outputColorSpace=T.SRGBColorSpace;renderer.shadowMap.enabled=true;V.prepend(renderer.domElement);const controls=new OrbitControls(camera,renderer.domElement);controls.enableDamping=true;
scene.add(new T.HemisphereLight(0xffffff,0x8093a3,2.4));const light=new T.DirectionalLight(0xffffff,3);light.position.set(-3,6,-4);scene.add(light);
const mats={paper:new T.MeshStandardMaterial({color:'#f4f0e6',roughness:.9}),edge:new T.MeshStandardMaterial({color:'#bba47d',roughness:1}),blue:new T.MeshStandardMaterial({color:'#0065bd',roughness:.9}),metal:new T.MeshStandardMaterial({color:'#718391',roughness:.55}),door:new T.MeshStandardMaterial({color:'#eee2c6',roughness:1}),red:new T.MeshStandardMaterial({color:'#ee542a',roughness:.7}),skin:new T.MeshStandardMaterial({color:'#d0a98b',roughness:.8}),shirt:new T.MeshStandardMaterial({color:'#faf1dc',roughness:1}),pants:new T.MeshStandardMaterial({color:'#3f667a',roughness:1}),hair:new T.MeshStandardMaterial({color:'#352822',roughness:1})};
function box(w,h,d,x,y,z,m,parent=scene){let a=new T.Mesh(new T.BoxGeometry(w,h,d),m);a.position.set(x,y,z);parent.add(a);return a}
function ball(r,p,m,parent=scene,scale){let a=new T.Mesh(new T.SphereGeometry(r,24,18),m);if(scale)a.scale.set(...scale);a.position.copy(p);parent.add(a);return a}
function link(a,b,r,m,parent=scene){const d=b.clone().sub(a),mesh=new T.Mesh(new T.CylinderGeometry(r,r,d.length(),18),m);mesh.position.copy(a).add(b).multiplyScalar(.5);mesh.quaternion.setFromUnitVectors(new T.Vector3(0,1,0),d.normalize());parent.add(mesh);return mesh}
function path(points,color,parent=scene,dashed=false){const g=new T.BufferGeometry().setFromPoints(points.map(a=>Array.isArray(a)?new T.Vector3(...a):a));let m=dashed?new T.LineDashedMaterial({color,dashSize:.035,gapSize:.025}):new T.LineBasicMaterial({color});let l=new T.Line(g,m);if(dashed)l.computeLineDistances();parent.add(l);return l}
function dim(a,b,color,parent=scene){path([a,b],color,parent);for(const p of[a,b])path([[p[0]-.035,p[1],p[2]],[p[0]+.035,p[1],p[2]]],color,parent)}
const texLoader=new T.TextureLoader(),loaded=[];function tex(f){let q=texLoader.load('./assets/'+f);q.colorSpace=T.SRGBColorSpace;loaded.push(q);return q}
const mask=tex('mask.png');mask.colorSpace=T.NoColorSpace;const brand=tex('brand.png'),stocks=[tex('stock-1.jpg'),tex('stock-2.jpg')],layla=tex('layla.png'),mct=tex('mct.png');
function print(w,h,p,texture,parent=scene,back=false,alpha){let mat=new T.MeshBasicMaterial({map:texture,transparent:true,side:T.DoubleSide,alphaTest:.2});if(alpha)mat.alphaMap=alpha;let a=new T.Mesh(new T.PlaneGeometry(w,h),mat);a.position.set(...p);if(back)a.rotation.y=Math.PI;parent.add(a);return a}
// One fabric plane, minimal stand; no solid exhibition wall.
const cloth=new T.Group();scene.add(cloth);box(3,3,.007,0,1.5,-1.5,mats.blue,cloth);print(1.3,1.3*289/409,[0,2.48,-1.492],brand,cloth);for(const x of[-1.52,1.52]){box(.025,3.05,.025,x,1.525,-1.52,mats.metal,cloth);box(.35,.02,.3,x,.01,-1.52,mats.metal,cloth)}
// Inset paper storage body and two doors, main tabletop750mm.
box(1.4,.65,.5,0,.325,0,mats.paper);box(2,.1,1,0,.70,0,mats.paper);box(1.7,.1,.65,0,.8,0,mats.paper);
for(const x of[-.3,.3]){box(.596,.506,.01,x,.325,.256,mats.door);box(.008,.09,.015,x<0?-.025:.025,.325,.27,mats.metal)}
const board=new T.Group();scene.add(board);const boardCy=.85+D.board_envelope[1]/2,W=D.board_envelope[0],PH=W*289/409;
function buildBoard(depth){disposeGroup(board);const face=depth/2;const matBack=new T.MeshStandardMaterial({color:'#0065ac',alphaMap:mask,transparent:true,alphaTest:.4,side:T.DoubleSide,roughness:.95});for(const z of[-face,face]){let a=new T.Mesh(new T.PlaneGeometry(W,PH),matBack);a.position.set(0,boardCy,z);board.add(a)}
// Original mask controls visible surfaces; core is inset and not a new silhouette.
for(let x=-.5;x<=.5;x+=.125)box(.004,.60,depth-.012,x,boardCy,0,mats.edge,board);
print(.85,.85*289/409,[0,boardCy,face+.001],brand,board);for(const [x,t]of[[-.27,layla],[.27,mct]])print(.38,.38*289/409,[x,1.21,face+.003],t,board);
for(const x of[-.55,.55]){let g=new T.Shape();g.moveTo(-.15,0);g.lineTo(.15,0);g.lineTo(0,.28);g.closePath();let me=new T.Mesh(new T.ExtrudeGeometry(g,{depth:.008,bevelEnabled:false}),mats.paper);me.rotation.y=Math.PI/2;me.position.set(x,.85,0);board.add(me)}
const top=new Set([0,1,2,3]),stockMeshes=[];
for(const slot of D.slots){const y=slot.hook_y,x=slot.x;
 link(new T.Vector3(x,y,-face),new T.Vector3(x,y,-face-.054),.002,mats.metal,board);link(new T.Vector3(x,y,-face-.054),new T.Vector3(x,y+.009,-face-.054),.002,mats.metal,board);
 const a=print(.145,.145*289/409,[x,y-.045,-face-.056],stocks[slot.i%2],board,true,mask);a.userData={slot:slot.i,hookHeight:y};stockMeshes.push(a);
 if(top.has(slot.i)){const ww=.154,hh=.114;path([[x-ww/2,y-.045-hh/2,-face-.058],[x+ww/2,y-.045-hh/2,-face-.058],[x+ww/2,y-.045+hh/2,-face-.058],[x-ww/2,y-.045+hh/2,-face-.058],[x-ww/2,y-.045-hh/2,-face-.058]],'#e94c25',board);ball(.009,new T.Vector3(x,y,-face-.064),mats.red,board)}
}
}
buildBoard(.14);
const floor=new T.Mesh(new T.PlaneGeometry(14,14),new T.MeshStandardMaterial({color:'#dfe5e8',roughness:1}));floor.rotation.x=-Math.PI/2;floor.position.y=-.005;scene.add(floor);const grid=new T.GridHelper(8,32,0xbac8d0,0xd0dade);grid.position.y=.001;scene.add(grid);
const human=new T.Group();scene.add(human);const annotations=new T.Group();scene.add(annotations);let shift=0,stand=.12,arm=.6448,depth=.14,view='back';
const labels=document.querySelector('#labels');let tags=[];function tag(id,point,html,cls='',dx=0,dy=0){let el=document.createElement('div');el.className='tag '+cls;el.innerHTML=html;labels.append(el);tags.push({id,point,el,dx,dy})}
function disposeGroup(group){while(group.children.length){const a=group.children.pop();a.traverse(o=>{if(o.geometry)o.geometry.dispose()});a.parent=null}}
function update(){disposeGroup(human);disposeGroup(annotations);labels.innerHTML='';tags=[];board.position.z=-shift;
 const h=D.highest,x=h.x,shoulderY=D.shoulder_height,sZ=-.5-stand,bodyX=x-.16;
 const shoulder=new T.Vector3(x,shoulderY,sZ),target=new T.Vector3(x,D.lift_y,-depth/2-.054-shift),delta=target.clone().sub(shoulder),dist=delta.length(),end=shoulder.clone().add(delta.clone().normalize().multiplyScalar(Math.min(dist,arm)));
 // Explicit 160cm manikin. Mean-proportion arm. Individual anatomy not inferred from height alone.
 const ankleY=.075,kneeY=.43,hipY=.84;
 for(const xx of[bodyX-.095,bodyX+.095]){box(.085,.055,.23,xx,.0275,sZ+.065,mats.paper,human);let ankle=new T.Vector3(xx,ankleY,sZ),knee=new T.Vector3(xx,kneeY,sZ),hip=new T.Vector3(xx,hipY,sZ);link(ankle,knee,.043,mats.pants,human);link(knee,hip,.055,mats.pants,human)}
 box(.27,.17,.17,bodyX,.85,sZ,mats.pants,human);box(.30,.32,.18,bodyX,1.105,sZ,mats.shirt,human);ball(.115,new T.Vector3(bodyX,1.485,sZ),mats.skin,human,[.80,1, .82]);ball(.118,new T.Vector3(bodyX,1.482,sZ-.025),mats.hair,human,[.85,1, .65]);link(new T.Vector3(bodyX,1.265,sZ),new T.Vector3(bodyX,1.40,sZ),.043,mats.skin,human);
 let ls=new T.Vector3(bodyX-.16,shoulderY,sZ),le=new T.Vector3(bodyX-.17,1.025,sZ+.02),lw=new T.Vector3(bodyX-.17,.80,sZ+.06);link(ls,le,.033,mats.shirt,human);link(le,lw,.025,mats.skin,human);ball(.027,lw,mats.skin,human);
 let L1=.3008,L2=Math.max(.23,arm-L1),d=Math.min(end.distanceTo(shoulder),L1+L2-.00001),u=end.clone().sub(shoulder).normalize(),aa=(L1*L1-L2*L2+d*d)/(2*d),hh=Math.sqrt(Math.max(0,L1*L1-aa*aa)),perp=new T.Vector3(0,-u.z,u.y).normalize(),elbow=shoulder.clone().add(u.clone().multiplyScalar(aa)).add(perp.multiplyScalar(hh));
 link(shoulder,elbow,.033,mats.shirt,human);const forehand=end.clone().sub(elbow),wrist=elbow.clone().add(forehand.clone().multiplyScalar(.232/L2));link(elbow,wrist,.024,mats.skin,human);link(wrist,end,.017,mats.skin,human);ball(.021,end,mats.skin,human);
 const hookZ=-depth/2-.054-shift;dim([x+.35,0,hookZ],[x+.35,h.hook_y,hookZ],'#cf401f',annotations);path([[x,h.hook_y,hookZ],[x+.35,h.hook_y,hookZ]],'#cf401f',annotations);ball(.012,target,mats.red,annotations);
 dim([bodyX-.30,0,sZ],[bodyX-.30,1.6,sZ],'#08705b',annotations);path([[x,shoulderY,sZ],[x,shoulderY,hookZ]],'#1464a5',annotations,true);path([shoulder,target],dist<=arm?'#c76c14':'#d53c30',annotations,true);
 let arc=[];for(let a=-.15;a<=1.55;a+=.025)arc.push([x,shoulderY+arm*Math.sin(a),sZ+arm*Math.cos(a)]);path(arc,'#df9b32',annotations,true);let touchArc=[];for(let a=-.15;a<=1.55;a+=.025)touchArc.push([x,shoulderY+(arm+.0608)*Math.sin(a),sZ+(arm+.0608)*Math.cos(a)]);path(touchArc,'#7895bb',annotations,true);
 if(dist>arm)path([end,target],'#d33d32',annotations);
 const margin=(arm-dist)*1000,horiz=Math.abs(target.z-sZ)*100;
 tag('human',new T.Vector3(bodyX-.30,1.61,sZ),'<strong>人物 160cm</strong>脚掌平放 / 身体直立','human',-90,-40);
 tag('hook',new T.Vector3(x+.35,h.hook_y,hookZ),`<strong>最高挂钩 ${(h.hook_y*100).toFixed(1)}cm</strong>商品上缘166.2 / 下缘155.7cm<br>最高排4个挂位橙红标出`,'high',20,-20);
 tag('lift',target.clone(),`<strong>抬起拿取 ${(D.lift_y*100).toFixed(1)}cm</strong>暂按越过钩头再抬3cm`,'high',view==='side'?20:-150,-80);
 tag('distance',new T.Vector3(x,shoulderY,(sZ+hookZ)/2),`前伸约 ${horiz.toFixed(1)}cm<br>从肩到钩端，不只看垂直高度`,'',view==='side'?-80:-100,50);
 tag('table',new T.Vector3(1,.75,.45),'<strong>主桌面 75cm</strong>桌深100cm / 桌身内收','',-90,20);
 if(view==='overall')tag('cloth',new T.Vector3(-1.3,2.95,-1.5),'<strong>背景布 3×3m</strong>仅一片布 + 一个纸中岛','',0,-30);
 document.querySelector('#standValue').textContent=Math.round(stand*100)+'cm';document.querySelector('#depthValue').textContent=Math.round(depth*100)+'cm';document.querySelector('#armValue').textContent=(arm*100).toFixed(1)+'cm';document.querySelector('#verdict').textContent=dist<=arm?(margin<40?'模型内勉强可取，已接近全伸；不能当作轻松自取位。':'模型内可达余量增加；仍需这位姑娘实测取下动作。'):(dist<=arm+.0608?'指尖可碰到，但捏取距离不够；无法完成取下动作。':'当前模型指尖与捏取都够不到，不能完成取下。');
 document.querySelector('#summary').innerHTML=`计算所需肩至捏取距离 <b>${(dist*100).toFixed(1)}cm</b>；模型捏取半径 ${(arm*100).toFixed(1)}cm；余量 ${(margin/10).toFixed(1)}cm。<br>肩高按平均比例约130.9cm；头顶160cm不是手部极限。`;
 document.querySelector('#ribbon').innerHTML=`<b>${shift?'对比提案：主牌向背面取货侧移15cm（未选定）':'当前布置：主牌居中'}</b> · 最高钩165.4cm，取下168.4cm；当前前伸 ${horiz.toFixed(1)}cm。<br>此为平均人体比例的几何校核，非实测人体或生产开孔图。橙弧=捏取，蓝弧=指尖。原实物挂位仅用于定位最高排；纸撑及重心需另核。`;
 window.reachReview.metrics={humanHeight:1.6,highestHook:h.hook_y,lift:D.lift_y,horizontal:Math.abs(target.z-sZ),required:dist,arm,margin:margin/1000,marginMm:margin,reachable:dist<=arm,touchReachable:dist<=arm+.0608,boardThickness:depth,shift,stand,highestCount:4,stockCount:26};
}
function setView(v){view=v;cloth.visible=v==='overall';for(const b of document.querySelectorAll('[data-view]'))b.classList.toggle('active',b.dataset.view===v);if(v==='back'){camera.position.set(2.5,2.25,-4.7);controls.target.set(0,1.0,-.16)}else if(v==='side'){camera.position.set(4.4,1.85,-.15);controls.target.set(0,1.0,-.25)}else{camera.position.set(4.0,3.1,4.8);controls.target.set(0,1.35,-.40)}controls.update();update()}
function setShift(v){shift=v;document.querySelector('#original').classList.toggle('active',!v);document.querySelector('#shifted').classList.toggle('active',!!v);update()}
window.reachReview={setView,setShift,setStand(v){stand=v;document.querySelector('#stand').value=v*100;update()},setArm(v){arm=v;document.querySelector('#arm').value=v*100;update()},setDepth(v){depth=v;document.querySelector('#depth').value=v*100;buildBoard(v);update()},metrics:{},capture(){renderer.render(scene,camera);return renderer.domElement.toDataURL('image/png')}};
for(const b of document.querySelectorAll('[data-view]'))b.onclick=()=>setView(b.dataset.view);document.querySelector('#original').onclick=()=>setShift(0);document.querySelector('#shifted').onclick=()=>setShift(.15);document.querySelector('#stand').oninput=e=>{stand=+e.target.value/100;update()};document.querySelector('#arm').oninput=e=>{arm=+e.target.value/100;update()};
document.querySelector('#depth').oninput=e=>{depth=+e.target.value/100;buildBoard(depth);update()};const resize=()=>{renderer.setSize(V.clientWidth,V.clientHeight);camera.aspect=V.clientWidth/V.clientHeight;camera.updateProjectionMatrix()};new ResizeObserver(resize).observe(V);resize();setView('back');document.querySelector('#busy').remove();
const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');Object.assign(svg.style,{position:'absolute',inset:0,width:'100%',height:'100%',pointerEvents:'none'});V.insertBefore(svg,labels);
function animate(){requestAnimationFrame(animate);controls.update();renderer.render(scene,camera);svg.innerHTML='';const ww=V.clientWidth,hh=V.clientHeight,small=ww<700;const pos=small?{human:[.04,.18],hook:[.04,.34],lift:[.04,.04],distance:[.04,.50],table:[.04,.80]}:view==='side'?{human:[.76,.22],hook:[.08,.36],lift:[.08,.21],distance:[.08,.51],table:[.12,.79]}:{human:[.72,.27],hook:[.08,.35],lift:[.08,.20],distance:[.08,.52],table:[.12,.78],cloth:[.10,.05]};
for(const t of tags){let p=t.point.clone().project(camera),hide=p.z>1||(view==='overall'&&!['table','cloth'].includes(t.id));t.el.style.display=hide?'none':'block';if(hide)continue;let px=(p.x*.5+.5)*ww,py=(-p.y*.5+.5)*hh,q=pos[t.id]||[.08,.1],lx=q[0]*ww,ly=q[1]*hh;t.el.style.left=lx+'px';t.el.style.top=ly+'px';let x2=Math.min(Math.max(px,lx),lx+t.el.offsetWidth),y2=Math.min(Math.max(py,ly),ly+t.el.offsetHeight),l=document.createElementNS('http://www.w3.org/2000/svg','line');for(const[k,v]of Object.entries({x1:px,y1:py,x2,y2,stroke:t.id==='human'?'#08705b':'#8195a2','stroke-width':1}))l.setAttribute(k,v);svg.append(l)}}animate();
