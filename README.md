# pGlyco2 beta2 (version 2.2.2, release date: 20191224)

![pGlyco2 workflow](https://github.com/pFindStudio/pGlyco2/blob/master/image/pGlyco2Flow.jpg)

Download it [here](https://github.com/pFindStudio/pGlyco2/releases/download/pGlyco2/pGlycoSetup.exe) or at pFind [website](http://pfind.ict.ac.cn/download/pGlyco/pGlycoSetup.exe).

[pFind Studio](http://pfind.ict.ac.cn) is computational solution for mass spectrometry-based proteomics, the newest version of pFind Studio includes pFind3 for proteomics, pLink2 for cross-linking proteomics, pNovo for de novo sequencing, pTop for intact protein analysis and pGlyco2 for intact glycopeptide analysis. 

If you have any question, please contact pglyco[at]ict.ac.cn, or you can post [issues](https://github.com/pFindStudio/pGlyco2/issues) at Github. To post github [issues](https://github.com/pFindStudio/pGlyco2/issues), see [github.pdf](http://pfind.ict.ac.cn/file/github.pdf) for details.

### Release Notes ###

#### pGlyco2.2.2 (2020.12.24): [User Guide](http://pfind.ict.ac.cn/software/pGlyco/pGlyco2%20User%20Guide.pdf) and [Download](http://pfind.ict.ac.cn/download/pGlyco/pGlycoSetup.exe) ####
* Multi-process for parsing the raw files.

#### pGlyco2.2.0 (2019.01.01): [User Guide](http://pfind.ict.ac.cn/software/pGlyco/pGlyco2%20User%20Guide.pdf) and [Download](http://pfind.ict.ac.cn/download/pGlyco/pGlyco2.2.0.exe) ####
* Fixed potential divide-zero bugs in pGlycoFDR.exe.
* Some improvements in gLabel.
* Supported mzML.
* Since Thermo has developed new raw APIs (RawFileReader.dll, same as Proteome Discoverer), xtract_raw and pParse were re-developed by using these new APIs, and it may introduce some differences compared with the old APIs. **If you need to change back to the MSFileReader-based APIs, please rename the xtract_raw_with_msfilereader.exe in the installation folder as xtract_raw.exe, and of course you need to install MSFileReader.**

#### pGlyco2.1.2: [User Guide](http://pfind.ict.ac.cn/software/pGlyco/pGlyco2.1.2%20User%20Guide.pdf) and [Download](http://pfind.ict.ac.cn/download/pGlyco/pGlyco2.1.2.exe) ####
* Fixed divide-zero bugs in pGlycoFDR.exe.
* gLabel supports batch plot and user-defined glycopeptides.
* Fixed GUI bugs in French Windows system (different types of float point).
* pGlyco.exe does not need administrator authorization to run.
