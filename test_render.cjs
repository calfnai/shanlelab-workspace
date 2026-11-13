// Execute the real generic page renderer with a minimal DOM (no dependencies).
const {readFileSync}=require('node:fs');
const vm=require('node:vm');
const assert=require('node:assert/strict');
const data=JSON.parse(readFileSync('site/data.js','utf8').slice('window.WORKSPACE='.length,-1));
const elements=new Map();
const element=selector=>{
  if(!elements.has(selector))elements.set(selector,{innerHTML:'',classList:{add(){},remove(){},toggle(){}},showModal(){this.open=true;},close(){this.open=false;}});
  return elements.get(selector);
};
const context=vm.createContext({
  window:{WORKSPACE:data,addEventListener(){}},
  document:{querySelector:element,querySelectorAll:()=>[],addEventListener(){}},
  location:{hash:'#hangzhou-xinwuji-space'},
  history:{replaceState(){}},setTimeout,clearTimeout,encodeURI,encodeURIComponent
});
vm.runInContext(readFileSync('site/app.js','utf8'),context);
assert.match(element('#content').innerHTML,/<h1>杭州新物集 SPACE<\/h1>/);
assert.match(element('#content').innerHTML,/documents\/hangzhou-space-oval-stand-20261113\/concept.png/);
context.showImage(0);
assert.equal(element('#lightbox').open,true);
assert.equal(element('#full-image').src,'documents/hangzhou-space-oval-stand-20261113/concept.png');
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
assert.match(element('#content').innerHTML,/杭州新物集 SPACE/);
console.log(`PASS: ${routes} generic project routes, all progress records, sparse progress, home and Hangzhou image dialog`);
