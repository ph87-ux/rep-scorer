const fs=require('fs'); const HZ=60, DT=1000/HZ, G=9.84;
function make(name, stroke, seed){
  let s=seed; const rnd=()=>{s=(s*1103515245+12345)&0x7fffffff; return s/0x7fffffff;};
  const nrm=()=>{let u=0,v=0;while(!u)u=rnd();while(!v)v=rnd();
    return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);};
  const rows=['t_ms,magnitude']; let t=0;
  const push=az=>{const at=nrm()*0.11, nz=nrm()*0.044;
    rows.push(t.toFixed(1)+','+Math.sqrt(Math.pow(G+az+nz,2)+at*at).toFixed(4)); t+=DT;};
  const still=sec=>{for(let i=0;i<Math.round(sec*HZ);i++)push(0);};
  const st=(d,T)=>{const A=Math.PI*Math.PI*stroke/(2*T*T),n=Math.round(T*HZ);
    for(let i=0;i<n;i++)push(d*A*Math.cos(Math.PI*i/n));};
  still(2.5);
  for(let i=0;i<8;i++){ st(1,4); still(2); st(-1,4); still(2); }
  still(2);
  fs.writeFileSync(name, rows.join('\n'));
}
make('a220.csv',0.220,11); make('a300.csv',0.300,11); make('a150.csv',0.150,11);
console.log('a150 / a220 / a300: 16 strokes each, exactly 150mm / 220mm / 300mm');
