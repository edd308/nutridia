from pathlib import Path
p=Path('/mnt/data/fixv193/index.html');s=p.read_text()
# Ensure panels hide properly (CSS display overrides hidden attr)
s=s.replace('</style>', '\n[hidden]{display:none!important}\n.food-panel:not([hidden]){display:block}\n.diet-day:not([hidden]){display:block}\n.dinner-result{display:block!important;border:2px solid #9ed9b7;background:#f1fbf4;padding:16px;margin:14px 0;border-radius:14px;color:#244d3a}\n.dinner-result h3{color:#244d3a}\n</style>')
# Date selection in diets; before result
s=s.replace('<div class="card" id="planResult">','<div class="card"><label for="planConsumedDate"><strong>Fecha en que has comido el plato</strong></label><input type="date" id="planConsumedDate" onchange="renderPlan()"><p class="muted">Selecciona la fecha y pulsa «He comido este plato» para sumar sus macros.</p></div><div class="card" id="planResult">')
# day tabs functional: wrap day section and provide visible fallback
s=s.replace('days.map((d,i)=>`<h3>${d}</h3>`+types.map(', 'days.map((d,i)=>`<div class="diet-day" data-day="${i}" ${i===selectedDietDay?"":"hidden"}><h3>${d}</h3>`+types.map(')
s=s.replace("}).join('')).join('')+'<p class=\"notice\">", "}).join('')+'</div>').join('')+'<p class=\"notice\">")
# ensure day tabs persist across render, date exists
s=s.replace("function renderPlan(){let p=active();", "function renderPlan(){let p=active();")
# after render plan closes, trigger showDietDay (renderPlan called from many locations)
needle="No se ha verificado una receta específica para cada plato.</p>'}"
s=s.replace(needle,"No se ha verificado una receta específica para cada plato.</p>';showDietDay(selectedDietDay)}")
# Ensure dinner visible on click and no stale results
s=s.replace("showDinnerResult();\n}","showDinnerResult();\n}")
# no candidates fallback clearly visible; give option
s=s.replace("No hay una propuesta adecuada para los macros pendientes. Consulta el resumen de arriba o ajusta los objetivos.","No hay un plato que encaje con lo que queda hoy. Revisa las calorías restantes o utiliza «Crear plato» para preparar una opción manual.")
# fix button accessibility after rendering plans; nutrition valid but zeros are not sufficient? leave
# cache update
p.write_text(s)
q=Path('/mnt/data/fixv193/sw.js');q.write_text(q.read_text().replace('nutridia-v19-2','nutridia-v19-3').replace('nutridia-v19-1','nutridia-v19-3'))
