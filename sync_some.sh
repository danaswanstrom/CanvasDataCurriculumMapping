
canvasDataCli fetch -c config.js -f wiki_dim
canvasDataCli fetch -c config.js -f wiki_page_dim
canvasDataCli fetch -c config.js -f wiki_fact
canvasDataCli fetch -c config.js -f wiki_page_fac
canvasDataCli unpack -c config.js -f wiki_dim
canvasDataCli unpack -c config.js -f wiki_page_dim
canvasDataCli unpack -c config.js -f wiki_fact
canvasDataCli unpack -c config.js -f wiki_page_fact

