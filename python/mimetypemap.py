
# dictionary of file extensions to mime-type
mime_type_map = {'bat': 'application/x-bat',
    'cmd': 'application/x-bat',
    'bpm': 'application/bizagi-modeler',
    'cbor': 'application/cbor',
    'cdr': 'application/coreldraw',
    'ditamap': 'application/dita+xml;format=map',
    'dita': 'application/dita+xml;format=topic',
    'ditaval': 'application/dita+xml;format=val',
    'epub': 'application/epub+zip',
    'fits': 'application/fits',
    'fit': 'application/fits',
    'fts': 'application/fits',
    'ai': 'application/illustrator',
    'idml': 'application/vnd.adobe.indesign-idml-package',
    'jar': 'application/java-archive',
    'js': 'application/javascript',
    'class': 'application/java-vm',
    'jnilib': 'application/x-java-jnilib',
    'hprof': 'application/vnd.java.hprof ',
    'ma': 'application/mathematica',
    'nb': 'application/mathematica',
    'mb': 'application/mathematica',
    'wl': 'application/vnd.wolfram.wl',
    'mp4': 'application/mp4',
    'doc': 'application/msword',
    'dot': 'application/msword',
    'onetoc': 'application/onenote;format=onetoc2',
    'onetoc2': 'application/onenote;format=onetoc2',
    'onepkg': 'application/onenote; format=package',
    'pdf': 'application/pdf',
    'ps': 'application/postscript',
    'eps': 'application/postscript',
    'epsf': 'application/postscript',
    'epsi': 'application/postscript',
    'rdf': 'application/rdf+xml',
    'owl': 'application/rdf+xml',
    'df$': 'application/rdf+xml',
    'wl$': 'application/rdf+xml',
    'xmp': 'application/rdf+xml',
    'rtf': 'application/rtf',
    'srl': 'application/sereal',
    'smi': 'application/smil+xml',
    'smil': 'application/smil+xml',
    'sml': 'application/smil+xml',
    'sldprt': 'application/sldworks',
    'sldasm': 'application/sldworks',
    'slddrw': 'application/sldworks',
    'asice': 'application/vnd.etsi.asic-e+zip',
    'asics': 'application/vnd.etsi.asic-s+zip',
    'fdf': 'application/vnd.fdf',
    'kml': 'application/vnd.google-earth.kml+xml',
    'nar': 'application/vnd.iptc.g2.newsmessage+xml',
    'chrt': 'application/vnd.kde.kchart',
    'kpr': 'application/vnd.kde.kpresenter',
    'kpt': 'application/vnd.kde.kpresenter',
    'ksp': 'application/vnd.kde.kspread',
    'kwd': 'application/vnd.kde.kword',
    'kwt': 'application/vnd.kde.kword',
    'skp': 'application/vnd.koan',
    'skd': 'application/vnd.koan',
    'skt': 'application/vnd.koan',
    'skm': 'application/vnd.koan',
    'mif': 'application/vnd.mif',
    'mmp': 'application/vnd.mindjet.mindmanager',
    'mmap': 'application/vnd.mindjet.mindmanager',
    'mmpt': 'application/vnd.mindjet.mindmanager',
    'mmat': 'application/vnd.mindjet.mindmanager',
    'mmmp': 'application/vnd.mindjet.mindmanager',
    'mmas': 'application/vnd.mindjet.mindmanager',
    'xls': 'application/vnd.ms-excel',
    'xlm': 'application/vnd.ms-excel',
    'xla': 'application/vnd.ms-excel',
    'xlc': 'application/vnd.ms-excel',
    'xlt': 'application/vnd.ms-excel',
    'xlw': 'application/vnd.ms-excel',
    'xll': 'application/vnd.ms-excel',
    'xld': 'application/vnd.ms-excel',
    'xlam': 'application/vnd.ms-excel.addin.macroenabled.12',
    'xlsm': 'application/vnd.ms-excel.sheet.macroenabled.12',
    'xlsb': 'application/vnd.ms-excel.sheet.binary.macroenabled.12',
    'msg': 'application/vnd.ms-outlook',
    'pst': 'application/vnd.ms-outlook-pst',
    'ost': 'application/vnd.ms-outlook-pst',
    'ppt': 'application/vnd.ms-powerpoint',
    'ppz': 'application/vnd.ms-powerpoint',
    'pps': 'application/vnd.ms-powerpoint',
    'pot': 'application/vnd.ms-powerpoint',
    'ppa': 'application/vnd.ms-powerpoint',
    'ppam': 'application/vnd.ms-powerpoint.addin.macroenabled.12',
    'pptm': 'application/vnd.ms-powerpoint.presentation.macroenabled.12',
    'ppsm': 'application/vnd.ms-powerpoint.slideshow.macroenabled.12',
    'docm': 'application/vnd.ms-word.document.macroenabled.12',
    'dotm': 'application/vnd.ms-word.template.macroenabled.12',
    'xps': 'application/vnd.ms-xpsdocument',
    'oxps': 'application/vnd.ms-xpsdocument',
    'odc': 'application/vnd.oasis.opendocument.chart',
    'otc': 'application/vnd.oasis.opendocument.chart-template',
    'odf': 'application/vnd.oasis.opendocument.formula',
    'odft': 'application/vnd.oasis.opendocument.formula-template',
    'odg': 'application/vnd.oasis.opendocument.graphics',
    'otg': 'application/vnd.oasis.opendocument.graphics-template',
    'odi': 'application/vnd.oasis.opendocument.image',
    'oti': 'application/vnd.oasis.opendocument.image-template',
    'odp': 'application/vnd.oasis.opendocument.presentation',
    'otp': 'application/vnd.oasis.opendocument.presentation-template',
    'ods': 'application/vnd.oasis.opendocument.spreadsheet',
    'ots': 'application/vnd.oasis.opendocument.spreadsheet-template',
    'odt': 'application/vnd.oasis.opendocument.text',
    'fodt': 'application/vnd.oasis.opendocument.flat.text',
    'fodp': 'application/vnd.oasis.opendocument.flat.presentation',
    'fods': 'application/vnd.oasis.opendocument.flat.spreadsheet',
    'otm': 'application/vnd.oasis.opendocument.text-master',
    'ott': 'application/vnd.oasis.opendocument.text-template',
    'oth': 'application/vnd.oasis.opendocument.text-web',
    'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    'thmx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    'potx': 'application/vnd.openxmlformats-officedocument.presentationml.template',
    'ppsx': 'application/vnd.openxmlformats-officedocument.presentationml.slideshow',
    'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'xltx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.template',
    'xltm': 'application/vnd.ms-excel.template.macroenabled.12',
    'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'dotx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.template',
    'sxw': 'application/vnd.sun.xml.writer',
    'pcap': 'application/vnd.tcpdump.pcap',
    'cap': 'application/vnd.tcpdump.pcap',
    'dmp': 'application/vnd.tcpdump.pcap',
    'vsd': 'application/vnd.visio',
    'vst': 'application/vnd.visio',
    'vss': 'application/vnd.visio',
    'vsw': 'application/vnd.visio',
    'vsdx': 'application/vnd.ms-visio.drawing',
    'vstx': 'application/vnd.ms-visio.template',
    'vssx': 'application/vnd.ms-visio.stencil',
    'vsdm': 'application/vnd.ms-visio.drawing.macroEnabled.12',
    'vstm': 'application/vnd.ms-visio.template.macroEnabled.12',
    'vssm': 'application/vnd.ms-visio.stencil.macroEnabled.12',
    'wmlc': 'application/vnd.wap.wmlc',
    'wmlsc': 'application/vnd.wap.wmlscriptc',
    'wpd': 'application/vnd.wordperfect',
    'wp': 'application/vnd.wordperfect',
    'wp5': 'application/vnd.wordperfect',
    'wp6': 'application/vnd.wordperfect',
    'w60': 'application/vnd.wordperfect',
    'wp61': 'application/vnd.wordperfect',
    'wpt': 'application/vnd.wordperfect',
    'warc': 'application/warc',
    'wasm': 'application/wasm',
    'tga': 'image/x-tga',
    'icb': 'image/x-tga',
    'vda': 'image/x-tga',
    'axx': 'application/x-axcrypt',
    'indd': 'application/x-adobe-indesign',
    'inx': 'application/x-adobe-indesign-interchange',
    'gtar': 'application/x-gtar',
    'bz2': 'application/x-bzip2',
    'tbz2': 'application/x-bzip2',
    'boz': 'application/x-bzip2',
    'vcd': 'application/x-cdlink',
    'crx': 'application/x-chrome-package',
    'cpio': 'application/x-cpio',
    'dex': 'application/x-dex',
    'dir': 'application/x-director',
    'dcr': 'application/x-director',
    'dxr': 'application/x-director',
    'cst': 'application/x-director',
    'cct': 'application/x-director',
    'cxt': 'application/x-director',
    'w3d': 'application/x-director',
    'fgd': 'application/x-director',
    'swa': 'application/x-director',
    'dvi': 'application/x-dvi',
    'elc': 'application/x-elc',
    'kil': 'application/x-killustrator',
    'exe': 'application/x-dosexec',
    'fp7': 'application/x-filemaker',
    'otf': 'application/x-font-otf',
    'ttf': 'application/x-font-ttf',
    'ttc': 'application/x-font-ttf',
    'afm': 'application/x-font-adobe-metric',
    'acfm': 'application/x-font-adobe-metric',
    'amfm': 'application/x-font-adobe-metric',
    'pfm': 'application/x-font-printer-metric',
    'spl': 'application/x-futuresplash',
    'grb': 'application/x-grib',
    'grb1': 'application/x-grib',
    'grb2': 'application/x-grib',
    'gz': 'application/gzip',
    'tgz': 'application/gzip',
    'zstd': 'application/zstd',
    'hdf': 'application/x-hdf',
    'he5': 'application/x-hdf',
    'h5': 'application/x-hdf',
    'ibooks': 'application/x-ibooks+zip',
    'arc': 'application/x-internet-archive',
    'iso': 'application/x-iso9660-image',
    'ipa': 'application/x-itunes-ipa',
    'latex': 'application/x-latex',
    'lz4': 'application/x-lz4',
    'lz': 'application/x-lzip',
    'lzma': 'application/x-lzma',
    'memgraph': 'application/x-memgraph',
    'prc': 'application/x-mobipocket-ebook',
    'mobi': 'application/x-mobipocket-ebook',
    'msi': 'application/x-ms-installer',
    'msp': 'application/x-ms-installer',
    'mst': 'application/x-ms-installer',
    'MYI': 'application/x-mysql-misam-compressed-index',
    'MYD': 'application/x-mysql-misam-data',
    'qpw': 'application/x-quattro-pro',
    'wb1': 'application/x-quattro-pro',
    'wb2': 'application/x-quattro-pro',
    'wb3': 'application/x-quattro-pro',
    'xq': 'application/xquery',
    'xquery': 'application/xquery',
    'rar': 'application/x-rar-compressed',
    'rpm': 'application/x-rpm',
    'sas': 'application/x-sas',
    'ss7': 'application/x-sas-program-data',
    'sas7bpgm': 'application/x-sas-program-data',
    'st7': 'application/x-sas-audit',
    'sas7baud': 'application/x-sas-audit',
    'sd2': 'application/x-sas-data-v6',
    'sd7': 'application/x-sas-data',
    'sas7bdat': 'application/x-sas-data',
    'sv7': 'application/x-sas-view',
    'sas7bvew': 'application/x-sas-view',
    'si7': 'application/x-sas-data-index',
    'sas7bndx': 'application/x-sas-data-index',
    'sc7': 'application/x-sas-catalog',
    'sas7bcat': 'application/x-sas-catalog',
    'sa7': 'application/x-sas-access',
    'sas7bacs': 'application/x-sas-access',
    'sf7': 'application/x-sas-fdb',
    'sas7bfdb': 'application/x-sas-fdb',
    'sm7': 'application/x-sas-mddb',
    'sas7bmdb': 'application/x-sas-mddb',
    's7m': 'application/x-sas-dmdb',
    'sas7bdmd': 'application/x-sas-dmdb',
    'sr7': 'application/x-sas-itemstor',
    'sas7bitm': 'application/x-sas-itemstor',
    'su7': 'application/x-sas-utility',
    'sas7butl': 'application/x-sas-utility',
    'sp7': 'application/x-sas-putility',
    'sas7bput': 'application/x-sas-putility',
    'stx': 'application/x-sas-transport',
    'sas7bbak': 'application/x-sas-backup',
    'xpt': 'application/x-sas-xport',
    'xport': 'application/x-sas-xport',
    'sh': 'application/x-sh',
    'bash': 'application/x-sh',
    'shp': 'application/x-shapefile',
    'swf': 'application/x-shockwave-flash',
    'sz': 'application/x-snappy-framed',
    'sfdu': 'application/x-sfdu',
    'do': 'application/x-stata-do',
    'dta': 'application/x-stata-dta',
    'tex': 'application/x-tex',
    'vmdk': 'application/x-vmdk',
    'xmind': 'application/x-xmind',
    'xml': 'application/xml',
    'xsl': 'application/xml',
    'xsd': 'application/xml',
    'mm': 'application/xml',
    'dicon': 'application/xml',
    'dtd': 'application/xml-dtd',
    'xslfo': 'application/xslfo+xml',
    'fo': 'application/xslfo+xml',
    'xslt': 'application/xslt+xml',
    'xspf': 'application/xspf+xml',
    'zip': 'application/zip',
    '7z': 'application/x-7z-compressed',
    'gdoc': 'application/vnd.google-apps.document',
    'gxls': 'application/vnd.google-apps.spreadsheet',
    'gppt': 'application/vnd.google-apps.presentation',
    'gform': 'application/vnd.google-apps.form',
    'gdraw': 'application/vnd.google-apps.drawing',
    'ghtml': 'application/vnd.google-apps.site',
    'au': 'audio/basic',
    'snd': 'audio/basic',
    'mid': 'audio/midi',
    'midi': 'audio/midi',
    'kar': 'audio/midi',
    'rmi': 'audio/midi',
    'mpga': 'audio/mpeg',
    'mp2': 'audio/mpeg',
    'mp2a': 'audio/mpeg',
    'mp3': 'audio/mpeg',
    'm2a': 'audio/mpeg',
    'm3a': 'audio/mpeg',
    'oga': 'audio/ogg',
    'ogg': 'audio/vorbis',
    'opus': 'audio/opus',
    'spx': 'audio/speex',
    'aif': 'audio/x-aiff',
    'aiff': 'audio/x-aiff',
    'aifc': 'audio/x-aiff',
    'caf': 'audio/x-caf',
    'flac': 'audio/x-flac',
    'm3u': 'audio/x-mpegurl',
    'ram': 'audio/x-pn-realaudio',
    'ra': 'audio/x-pn-realaudio',
    'rmp': 'audio/x-pn-realaudio-plugin',
    'wav': 'audio/x-wav',
    'weba': 'audio/webm',
    'pdb': 'chemical/x-pdb',
    'exr': 'image/aces',
    'bmp': 'image/bmp',
    'dib': 'image/bmp',
    'bpg': 'image/x-bpg',
    'cgm': 'image/cgm',
    'dpx': 'image/x-dpx',
    'emf': 'image/emf',
    'emz': 'image/x-emf-compressed',
    'gif': 'image/gif',
    'heif': 'image/heif',
    'heic': 'image/heic',
    'icns': 'image/icns',
    'jp2': 'image/jp2',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'jpe': 'image/jpeg',
    'jif': 'image/jpeg',
    'jfif': 'image/jpeg',
    'jfi': 'image/jpeg',
    'jpm': 'image/jpm',
    'jpgm': 'image/jpm',
    'jpf': 'image/jpx',
    'png': 'image/png',
    'svg': 'image/svg+xml',
    'svgz': 'image/svg+xml',
    'tiff': 'image/tiff',
    'tif': 'image/tiff',
    'psd': 'image/vnd.adobe.photoshop',
    'dwg': 'image/vnd.dwg',
    'dxb': 'image/vnd.dxb',
    'dxf': 'image/vnd.dxf',
    'mdi': 'image/vnd.ms-modi',
    'wbmp': 'image/vnd.wap.wbmp',
    'dcx': 'image/vnd.zbrush.dcx',
    'pcx': 'image/vnd.zbrush.pcx',
    'avif': 'image/avif',
    'wmf': 'image/wmf',
    'fh': 'image/x-freehand',
    'fhc': 'image/x-freehand',
    'fh4': 'image/x-freehand',
    'fh40': 'image/x-freehand',
    'fh5': 'image/x-freehand',
    'fh50': 'image/x-freehand',
    'fh7': 'image/x-freehand',
    'fh8': 'image/x-freehand',
    'fh9': 'image/x-freehand',
    'fh10': 'image/x-freehand',
    'fh11': 'image/x-freehand',
    'fh12': 'image/x-freehand',
    'ft7': 'image/x-freehand',
    'ft8': 'image/x-freehand',
    'ft9': 'image/x-freehand',
    'ft10': 'image/x-freehand',
    'ft11': 'image/x-freehand',
    'ft12': 'image/x-freehand',
    'jb2': 'image/x-jbig2',
    'jbig2': 'image/x-jbig2',
    'j2c': 'image/x-jp2-codestream',
    'pic': 'image/x-pict',
    'pct': 'image/x-pict',
    'pict': 'image/x-pict',
    'pnm': 'image/x-portable-anymap',
    'pbm': 'image/x-portable-bitmap',
    'pgm': 'image/x-portable-graymap',
    'ppm': 'image/x-portable-pixmap',
    'dng': 'image/x-raw-adobe',
    '3fr': 'image/x-raw-hasselblad',
    'raf': 'image/x-raw-fuji',
    'crw': 'image/x-raw-canon',
    'cr2': 'image/x-raw-canon',
    'k25': 'image/x-raw-kodak',
    'kdc': 'image/x-raw-kodak',
    'dcs': 'image/x-raw-kodak',
    'drf': 'image/x-raw-kodak',
    'mrw': 'image/x-raw-minolta',
    'nef': 'image/x-raw-nikon',
    'nrw': 'image/x-raw-nikon',
    'orf': 'image/x-raw-olympus',
    'ptx': 'image/x-raw-pentax',
    'pef': 'image/x-raw-pentax',
    'arw': 'image/x-raw-sony',
    'srf': 'image/x-raw-sony',
    'sr2': 'image/x-raw-sony',
    'x3f': 'image/x-raw-sigma',
    'erf': 'image/x-raw-epson',
    'mef': 'image/x-raw-mamiya',
    'mos': 'image/x-raw-leaf',
    'raw': 'image/x-raw-panasonic',
    'rw2': 'image/x-raw-panasonic',
    'iiq': 'image/x-raw-phaseone',
    'r3d': 'image/x-raw-red',
    'fff': 'image/x-raw-imacon',
    'pxn': 'image/x-raw-logitech',
    'bay': 'image/x-raw-casio',
    'rwz': 'image/x-raw-rawzor',
    'rgb': 'image/x-rgb',
    'xcf': 'image/x-xcf',
    'xwd': 'image/x-xwindowdump',
    'mht': 'multipart/related',
    'mhtml': 'multipart/related',
    'igs': 'model/iges',
    'iges': 'model/iges',
    'dwf': 'model/vnd.dwf',
    'dwfx': 'model/vnd.dwfx+xps',
    'as': 'text/x-actionscript',
    'ada': 'text/x-ada',
    'adb': 'text/x-ada',
    'ads': 'text/x-ada',
    'applescript': 'text/x-applescript',
    'asp': 'text/asp',
    'aspx': 'text/aspdotnet',
    'aj': 'text/x-aspectj',
    's': 'text/x-assembly',
    'asm': 'text/x-assembly',
    'css': 'text/css',
    'html': 'text/html',
    'htm': 'text/html',
    't': 'text/troff',
    'tr': 'text/troff',
    'roff': 'text/troff',
    'man': 'text/troff',
    'me': 'text/troff',
    'ms': 'text/troff',
    'gv': 'text/vnd.graphviz',
    'anpa': 'text/vnd.iptc.anpa',
    'wmls': 'text/vnd.wap.wmlscript',
    'vtt': 'text/vtt',
    'awk': 'text/x-awk',
    'bas': 'text/x-basic',
    'hpp': 'text/x-c++hdr',
    'hxx': 'text/x-c++hdr',
    'hh': 'text/x-c++hdr',
    'h++': 'text/x-c++hdr',
    'hp': 'text/x-c++hdr',
    'cpp': 'text/x-c++src',
    'cxx': 'text/x-c++src',
    'cc': 'text/x-c++src',
    'c++': 'text/x-c++src',
    'cgi': 'text/x-cgi',
    'h': 'text/x-chdr',
    'clj': 'text/x-clojure',
    'coffee': 'text/x-coffeescript',
    'c': 'text/x-csrc',
    'cs': 'text/x-csharp',
    'cbl': 'text/x-cobol',
    'cob': 'text/x-cobol',
    'cfm': 'text/x-coldfusion',
    'cfml': 'text/x-coldfusion',
    'cfc': 'text/x-coldfusion',
    'cl': 'text/x-common-lisp',
    'jl': 'text/x-common-lisp',
    'lisp': 'text/x-common-lisp',
    'lsp': 'text/x-common-lisp',
    'e': 'text/x-eiffel',
    'el': 'text/x-emacs-lisp',
    'erl': 'text/x-erlang',
    'exp': 'text/x-expect',
    '4th': 'text/x-forth',
    'f': 'text/x-fortran',
    'for': 'text/x-fortran',
    'f77': 'text/x-fortran',
    'f90': 'text/x-fortran',
    'go': 'text/x-go',
    'groovy': 'text/x-groovy',
    'hs': 'text/x-haskell',
    'lhs': 'text/x-haskell',
    'idl': 'text/x-idl',
    'ini': 'text/x-ini',
    'java': 'text/x-java-source',
    'properties': 'text/x-java-properties',
    'jsp': 'text/x-jsp',
    'less': 'text/x-less',
    'l': 'text/x-lex',
    'log': 'text/x-log',
    'lua': 'text/x-lua',
    'ml': 'text/x-ml',
    'm3': 'text/x-modula',
    'i3': 'text/x-modula',
    'mg': 'text/x-modula',
    'ig': 'text/x-modula',
    'm': 'text/x-objcsrc',
    'ocaml': 'text/x-ocaml',
    'mli': 'text/x-ocaml',
    'p': 'text/x-pascal',
    'pp': 'text/x-pascal',
    'pas': 'text/x-pascal',
    'dpr': 'text/x-pascal',
    'pl': 'text/x-perl',
    'pm': 'text/x-perl',
    'al': 'text/x-perl',
    'perl': 'text/x-perl',
    'php': 'text/x-php',
    'php3': 'text/x-php',
    'php4': 'text/x-php',
    'pro': 'text/x-prolog',
    'py': 'text/x-python',
    'rest': 'text/x-rst',
    'rst': 'text/x-rst',
    'restx': 'text/x-rst',
    'rexx': 'text/x-rexx',
    'rb': 'text/x-ruby',
    'scala': 'text/x-scala',
    'scm': 'text/x-scheme',
    'sed': 'text/x-sed',
    'sql': 'text/x-sql',
    'st': 'text/x-stsrc',
    'itk': 'text/x-tcl',
    'tcl': 'text/x-tcl',
    'tk': 'text/x-tcl',
    'cls': 'text/x-vbasic',
    'frm': 'text/x-vbasic',
    'vb': 'text/x-vbdotnet',
    'vbs': 'text/x-vbscript',
    'v': 'text/x-verilog',
    'vhd': 'text/x-vhdl',
    'vhdl': 'text/x-vhdl',
    'md': 'text/x-web-markdown',
    'mdtext': 'text/x-web-markdown',
    'mkd': 'text/x-web-markdown',
    'markdown': 'text/x-web-markdown',
    'y': 'text/x-yacc',
    'yaml': 'text/x-yaml',
    'mj2': 'video/mj2',
    'mjp2': 'video/mj2',
    'mpeg': 'video/mpeg',
    'mpg': 'video/mpeg',
    'mpe': 'video/mpeg',
    'm1v': 'video/mpeg',
    'm2v': 'video/mpeg',
    'ogv': 'video/ogg',
    'drc': 'video/x-dirac',
    'ogm': 'video/x-ogm',
    'qt': 'video/quicktime',
    'mov': 'video/quicktime',
    'webm': 'video/webm',
    'asx': 'application/x-ms-asx',
    'avi': 'video/x-msvideo',
    'ice': 'x-conference/x-cooltalk',
    'fb2': 'application/x-fictionbook+xml',
    'asciidoc': 'text/x-asciidoc',
    'adoc': 'text/x-asciidoc',
    'ad': 'text/x-asciidoc',
    'd': 'text/x-d',
    'haml': 'text/x-haml',
    'hx': 'text/x-haxe',
    'xlf': 'application/x-xliff+xml',
    'xliff': 'application/x-xliff+xml',
    'xlz': 'application/x-xliff+zip',
    'r': 'text/x-rsrc',
    'txt': 'text/plain',
    'csv': 'text/csv'
    }