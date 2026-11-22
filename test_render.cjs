// Execute the real generic page renderer with a minimal DOM (no dependencies).
const {readFileSync}=require('node:fs');
const vm=require('node:vm');
const assert=require('node:assert/strict');
const data=JSON.parse(readFileSync('site/data.js','utf8').slice('window.WORKSPACE='.length,-1));
const imageProject=data.projects.find(p=>!p.comparison&&!p.workbench&&p.items.length);
assert.ok(imageProject);
assert.ok(!data.projects.some(p=>p.id==='hangzhou-xinwuji-space'));
const elements=new Map();
const element=selector=>{
  if(!elements.has(selector))elements.set(selector,{innerHTML:'',classList:{add(){},remove(){},toggle(){}},showModal(){this.open=true;},close(){this.open=false;}});
  return elements.get(selector);
};
const context=vm.createContext({
  window:{WORKSPACE:data,addEventListener(){}},
  document:{querySelector:element,querySelectorAll:()=>[],addEventListener(){}},
  location:{hash:'#'+imageProject.id},
  history:{replaceState(){}},setTimeout,clearTimeout,encodeURI,encodeURIComponent
});
vm.runInContext(readFileSync('site/app.js','utf8'),context);
assert.ok(element('#content').innerHTML.includes(`<h1>${imageProject.title}</h1>`));
const currentImage=imageProject.items[0].file;
assert.ok(element('#content').innerHTML.includes(currentImage));
context.showImage(0);
assert.equal(element('#lightbox').open,true);
assert.equal(element('#full-image').src,currentImage);
let routes=0;
for(const p of data.projects){
  assert.doesNotThrow(()=>context.projectProgress(p),p.id);
  if(p.comparison||p.workbench)continue; // Dedicated renderers are outside this check.
  context.location.hash='#'+p.id;
  context.render();
  assert.ok(element('#content').innerHTML.includes(`<h1>${p.title}</h1>`),p.id);
  routes++;
}
for(const progress of [{},{next:null,decisions:null,history:null,sources:null}]){
  assert.doesNotThrow(()=>context.projectProgress({items:[],progress}));
}
context.location.hash='#home';context.render();
assert.ok(element('#content').innerHTML.includes(imageProject.title));
assert.ok(!element('#content').innerHTML.includes('hangzhou-xinwuji-space'));
context.location.hash='#hangzhou-xinwuji-space';context.render();
assert.ok(!element('#content').innerHTML.includes('<h1>杭州新物集 SPACE</h1>'));
console.log(`PASS: ${routes} generic project routes, all progress records, sparse progress, home, archived route exclusion and active image dialog`);
