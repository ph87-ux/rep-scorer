// Does transverse vibration inflate travel? |a| = sqrt((g+az)^2 + at^2) ~= g + az + at^2/(2g).
// The transverse term is ALWAYS positive, so a stack that rattles while it moves adds a
// positive bias to the only signal the app sees. Two identical 300mm sets, differing only in
// how much transverse noise there is while moving.
const fs=require('fs');
const HZ=60, DT=1000/HZ, G=9.84;
function g(){let u=0,v=0;while(!u)u=Math.random();while(!v)v=Math.random();
  return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);}
function make(name, sigStill, sigMove, seed){
  let s=seed; const rnd=()=>{s=(s*1103515245+12345)&0x7fffffff; return s/0x7fffffff;};
  const nrm=()=>{let u=0,v=0;while(!u)u=rnd();while(!v)v=rnd();
    return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);};
  const rows=['t_ms,magnitude']; let t=0;
  const push=(az,moving)=>{
    const sg = moving ? sigMove : sigStill;
    const at = nrm()*sg;                 // transverse, rectified by the magnitude
    const nz = nrm()*sigStill*0.4;       // a little vertical noise either way
    rows.push(t.toFixed(1)+','+Math.sqrt(Math.pow(G+az+nz,2)+at*at).toFixed(4)); t+=DT;};
  const still=sec=>{for(let i=0;i<Math.round(sec*HZ);i++)push(0,false);};
  const st=(d,T,stroke)=>{const A=Math.PI*Math.PI*stroke/(2*T*T),n=Math.round(T*HZ);
    for(let i=0;i<n;i++)push(d*A*Math.cos(Math.PI*i/n),true);};
  still(2.5);
  for(let i=0;i<6;i++){ st(1,4,0.30); still(2); st(-1,4,0.30); still(2); }
  still(2);
  fs.writeFileSync(name, rows.join('\n'));
}
make('quiet.csv', 0.110, 0.110, 7);   // same noise moving or still
make('rattle.csv', 0.110, 0.246, 7);  // the 2.2x rise measured on the real loaded set
console.log('quiet.csv and rattle.csv: 12 strokes of exactly 300mm each');
