key = {}
key['X'] = 'r'
key['g'] = 'e'
key['p'] = 'y'
key['G'] = 'o'
key['v'] = 'u'
key['L'] = 'k'
key['n'] = 'n'
key['G'] = 'o'
key['Y'] = 'w'
key['V'] = 'i'
key['T'] = 'f'
key['s'] = 'a'
key['F'] = 'c'
key['f'] = 's'
key['g'] = 'e'
key['H'] = 'v'
key['m'] = 't'
key['y'] = 'p'
key['v'] = 'u'
key['W'] = 'b'
key['U'] = 'l'
key['q'] = 'd'
key['c'] = 'm'
key['D'] = 'h'
key['e'] = 'g'
key['K'] = 'x'
string = list("pGv LnGY, VT pGv'Xg s FGnfgXHsmVHg XgyvWUVFsn, VT V YgXg s UVWgXsU, VT, UVLg, GL, VT V Xsn sf s UVWgXsU qgcGFXsm, mDgp YGvUq fsp V'c Gng GT mDg fcsXmgfm ygGyUg snpYDgXg Vn mDg YGXUq. nGWGqp LnGYf Vm, Wvm mDg TUse Vf vDgmGnUXVf. Wvm YDgn pGv'Xg s FGnfgXHsmVHg XgyvWUVFsn mDgp mXp. nvFUgsX Vf fG yGYgXTvU. eGGq egngf, HgXp eGGq egngf, GL, HgXp fcsXm, mDg YDsXmGn fFDGGU GT TVnsnFg, HgXp eGGq, HgXp fcsXm. UGGL, DsHVne nvFUgsX, cp vnFUg Ysf s eXgsm yXGTgffGX snq fFVgnmVfm snq gneVnggX, qGFmGX OGDn mXvcy sm cVm. nGY Vm vfgq mG Wg mDXgg, nGY Vm'f TGvX. Wvm mDg ygXfVsnf sXg eXgsm ngeGmVsmGXf, mDg VXsnVsnf sXg eXgsm ngeGmVsmGXf, fG, snq mDgp, mDgp Ovfm LVUUgq, mDgp Ovfm LVUUgq vf. TgUUsf, snq Vm Vf TgUUsf WgFsvfg, pGv LnGY, mDgp qGn'm, mDgp DsHgn'm TVevXgq mDsm mDg YGcgn sXg fcsXmgX XVeDm nGY mDsn mDg cgn, fG, pGv LnGY, Vm'f eGnns msLg mDgc sWGvm snGmDgX DvnqXgq snq TVTmp pgsXf. mDsm'f YDp V sUYspf fmsXm GTT, Ygnm mG YDsXmGn, Ysf s eGGq fmvqgnm, Ygnm mDgXg, Ygnm mDgXg, qVq mDVf, WvVUm s TGXmvng. cp vnFUg gKyUsVngq mDsm mG cg csnp, csnp pgsXf seG, mDg yGYgX snq mDsm Ysf mDVXmp TVHg pgsXf seG. Wvm YDgn pGv UGGL sm YDsm'f eGVne Gn YVmD mDg TGvX yXVfGngXf. Vm'f mXvg! GD, qG mDgp qG s nvcWgX. Wvm YDgn Vm Ysf mDXgg snq gHgn nGY, V YGvUq DsHg fsVq Vm'f sUU Vn mDg cgffgnegX. pGv LnGY V DsHg mG eVHg cp UVLg FXgqgnmVsUf sUU mDg mVcg, WgFsvfg Yg'Xg s UVmmUg qVfsqHsnmsegq. Wvm pGv UGGL sm mDg nvFUgsX qgsU, mDg mDVne mDsm XgsUUp WGmDgXf cg, Vm YGvUq DsHg Wggn fG gsfp, snq Vm'f nGm sf VcyGXmsnm sf mDgfg UVHgf sXg. Dg YGvUq gKyUsVn mDg yGYgX GT YDsm'f eGVne mG Dsyygn snq Dg Ysf XVeDm, YDG YGvUq DsHg mDGveDm?")
i = 0
while i < len(string):
	if(string[i] == ' '):
		i = i+1
		continue
	else:
		if string[i] in key:
			string[i] = key[string[i]]
		i=i+1
final = "".join(string)
print(final)
