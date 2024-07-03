def common_elements(fst_start=0, fst_end=100, fst_cond='% 3 == 0',
                    snd_start=0, snd_end=100, snd_cond='% 5 == 0'):

    fst_set = {x for x in range(fst_start, fst_end + 1) if eval('x' + fst_cond)}
    snd_set = {x for x in range(snd_start, snd_end + 1) if eval('x' + snd_cond)}

    return fst_set.intersection(snd_set)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')
