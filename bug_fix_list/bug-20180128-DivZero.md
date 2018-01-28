#### Divide by Zero bug in pGlycoFDR.exe ####

Sometimes all GlycoFDR or TotalFDR in the result file may become 1 because the "divide by zero" bug in pGlycoFDR.exe, hence there will be no results after filtering by TotalFDR <= 0.01.

Replace the pGlycoFDR.exe in %pglyco_install_path%/pGlyco2/bin folder with this [pGlycoFDR.exe](https://github.com/pFindStudio/pGlyco2/blob/master/bug_fix_list/fixed_file_2018/bug-20180128-DivZero/pGlycoFDR.exe.rename) (rename pGlycoFDR.exe.rename back to pGlycoFDR.exe after you download it.)
