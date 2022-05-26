import random
import time
import dns
import dns.resolver
import json

################################################################
def loadjson(file):
    with open(file,"r") as f:
        jsonld = json.loads(f.read())
        f.close()
        return jsonld

jls = loadjson("perfom.json")
servlist = jls["servlist"]
burpmode = jls["mode"]
################################################################
class ramdd:

    All = []
    Cm = []
    num = [0,1,2,3,4,5,6,7,8,9]
    def __init__(self):
        self.Alllist()
        self.Mklist()

    def Mklist(self):
        A = 65
        Z = 65 + 26
        a = 97
        z = 97 + 26
        Li = []
        for x in range(A, Z):
            Li.append(chr(x))
        for xx in range(a, z):
            Li.append(chr(xx))
        for xxx in range(1,10):
            Li.append(str(xxx))
        self.Cm = Li
        return Li

    def Alllist(self):
        Ali = []
        for x in range(128):
            Ali.append(chr(x))
        self.All = Ali
        return Ali

    def ramdschar(self,bit):
        res = ""
        limi = len(self.Cm)-1
        for x in range(bit):
            step = int(random.random()*(time.time())%600*100)
            res += self.Cm[step%limi]
        return res

    def randnum(self,bit,seet):
        res = ""
        limi = len(seet)
        for x in range(bit):
            step = int(random.randint(0,65535))
            res += str(seet[step % limi])
        return res

    def randnumlist(self,bit,rund):
        res = set()
        st = int("1"+"0"*(bit-1))
        ed = int("9"*bit)
        for x in range(rund):
            res.add(random.randint(st,ed))
        return res

def burp_rd(ine,bit):
    s = set()
    for x in range(ine):
        s.add(ramdd().randnum(bit,ramdd().num))
    return s

def burp_rc(ine,bit):
    s = set()
    for x in range(ine):
        s.add(ramdd().ramdschar(bit))
    return s

################################################################
## Clock list work like a clock
class defclock():
    le = 0
    bit = 0
    forl = None
    li = []
    stop = False
    def __init__(self,bit,le):
        self.forl = (le**bit)-1
        self.bit = bit
        self.le = le
        for x in range(self.bit):
            self.li.append(0)

    def tick(self):
        self.li[0]+=1
        add1 = False
        for x in range(len(self.li)):
            if add1:
                add1 = False
                self.li[x] += 1
            if self.li[x] >= self.le:
                add1 = True
                if self.li[-1] < self.le:
                    self.li[x] = 0
                else:
                    self.stop = True
        return self.li

################################################################
## Rand
class dictionary:
    dist = ["lele", "www", "mail", "ftp", "smtp", "pop", "m", "webmail", "pop3", "imap", "localhost", "autodiscover",
            "admin"
        , "bbs", "test.txt", "mx", "en", "email", "wap", "blog", "oa", "ns1", "vpn", "ns2", "www2", "mysql", "webdisk",
            "dev", "old", "news",
            "calendar", "shop", "potala", "mobile", "web", "sip", "mobilemail", "ns", "cpanel", "www1", "whm", "new",
            "img", "search", "support"
        , "mail2", "media", "files", "e", "video", "app", "secure", "my", "crm", "intranet", "portal", "demo", "api",
            "beta", "fax"
        , "lyncdiscover", "dns", "images", "db", "staging", "info", "docs", "static", "ns3", "download", "forum", "cms",
            "cdn", "www3",
            "wiki", "pda", "dns1", "home", "mail1", "online", "sso", "lists", "webproxy", "office", "dns2", "get", "t",
            "gis", "proxy", "pic",
            "edu", "d", "ns4", "cs", "cn", "b2b", "store", "community", "start", "services", "wx", "service",
            "training", "remote", "health",
            "help", "vip", "soft", "finance", "photo", "apps", "owa", "login", "es", "s", "ads", "stats", "events",
            "forums", "sc", "tv", "data",
            "jobs", "survey", "it", "hr", "sms", "game", "stage", "i", "send", "member", "v", "a", "ww", "sz", "live",
            "im", "go", "chat", "3g",
            "gateway", "library", "ftp2", "dialin", "security", "meet", "upload", "w", "blogs", "de", "image", "msoid",
            "hk", "down", "gmail",
            "ssh", "fr", "english", "exchange", "so", "av", "cp", "erp", "cloud", "legacy", "ldap", "ad", "sites",
            "access", "archive", "job",
            "connect", "hq", "alumni", "downloads", "extranet", "lib", "tools", "careers", "wt", "ask", "student",
            "host", "ns5", "helpdesk", "u", "vc", "status", "direct", "rs", "hb", "sp", "mailhost", "uk", "netmang",
            "svn", "tz", "ms", "sx", "zb", "metrics", "mx2", "hd", "ss", "qa", "dj", "www4", "bm", "jp", "file",
            "project", "club", "dl", "feeds", "IN", "ent", "ws", "food", "update", "tj", "book", "as", "gb", "lab",
            "targs", "dx", "js", "b", "sh", "cnc", "videos", "dns3", "outlook", "software", "auth", "tw", "preview",
            "hs", "git", "content", "press", "ir", "cq", "projects", "car", "monitor", "backup", "meeting", "c",
            "photos", "games", "radio", "gw", "public", "buy", "ssl", "mall", "research", "groups", "pt", "wwww",
            "forms", "music", "cx", "cj", "techmang", "bj", "math", "res", "mang", "open", "ntp", "w3", "biz", "ca",
            "map", "ru", "design", "share", "th", "relay", "house", "in", "vpn2", "x", "citrix", "labs", "pub",
            "education", "jw", "global", "tp", "card", "jk", "f", "gh", "sd", "www5", "rt", "reg", "us", "weather",
            "newsletter", "ticket", "server", "irc", "apple", "cache", "youth", "rms", "www0", "mx1", "feedback", "fz",
            "ams", "wh", "reports", "auto", "travel", "cm", "origin", "account", "site", "cc", "p", "vote", "bt", "ems",
            "manage", "pms", "dk", "sharepoint", "mssql", "partner", "spam", "lt", "link", "user", "tg", "sg",
            "business", "xx", "ly", "students", "ts", "fs", "vpn1", "dm", "uc", "digital", "cl", "pages", "abc",
            "brand", "event", "alpha", "sys", "assets", "0", "members", "money", "mdm", "sales", "stat", "local", "be",
            "tuan", "marketing", "bugs", "mail3", "dy", "time", "stream", "code", "partners", "view", "da", "g", "tr",
            "inside", "br", "phx", "st", "dms", "jj", "gallery", "wp", "shopping", "promo", "china", "social", "show",
            "union", "pm", "web1", "test2", "gc", "ja", "kb", "register", "sq", "pc", "maps", "android", "corp",
            "wireless", "pos", "ce", "rsc", "jira", "accounts", "customer", "jd", "list", "ec", "adm", "web2", "rtx",
            "corporate", "flash", "developer", "rss", "tour", "wl", "log", "smtp2", "sns", "sf", "cas", "directory",
            "webdev", "temp", "ps", "q", "idc", "sm", "ks", "bc", "hy", "fx", "tech", "bb", "tao", "weixin", "journal",
            "updates", "agent", "art", "hg", "ic", "mobi", "cd", "usa", "cr", "hao", "desktop", "ex", "ra", "teacher",
            "r", "ag", "dc", "jwc", "mrtg", "tu", "sj", "ace", "space", "ft", "lp", "fw", "mailgw", "mis", "co",
            "investors", "bookstore", "sql", "hermes", "ip", "3", "eq", "sandbox", "client", "css", "catalog", "sports",
            "sentry", "kr", "internal", "ky", "sy", "investor", "mms", "exam", "transfer", "ga", "summer", "conference",
            "hotel", "dz", "pro", "doc", "eng", "cf", "registration", "whois", "life", "world", "ae", "sts", "mp",
            "staff", "id", "push", "enterprise", "bi", "webservices", "idp", "pe", "prod", "mailgate", "top", "yy",
            "zw", "lms", "edm", "linux", "vps", "nj", "mm", "net", "z", "ml", "webcast", "phone", "manager", "cz",
            "ids", "smtp1", "work", "mars", "listserv", "campus", "special", "ee", "n", "au", "cw", "pay", "dealer",
            "barracuda", "6", "pp", "acs", "chem", "nl", "w2", "audio", "family", "xa", "multimedia", "jabber", "click",
            "international", "ct", "resource", "cal", "mailman", "links", "pl", "2", "stock", "movie", "atlas", "fm",
            "shanghai", "keys", "mi", "love", "product", "ls", "sb", "ch", "wb", "fb", "qc", "intra", "em", "dw",
            "cert", "hn", "yp", "noc", "fc", "main", "md", "ww2", "streaming", "master", "ma", "daj", "ny", "print",
            "bg", "nas", "me", "kids", "archives", "wms", "webadmin", "stu", "xb", "h", "xml", "asp", "server1",
            "order", "sync", "ftp1", "zp", "asia", "hz", "pa", "power", "signup", "hh", "history", "learning",
            "password", "nc", "edge", "gg", "storage", "hub", "ess", "yun", "opac", "test1", "jupiter", "fms", "123",
            "xl", "cvs", "crl", "ocs", "bz", "lb", "newsroom", "pf", "webstats", "market", "radius", "cwc", "tk", "int",
            "dt", "acc", "rd", "jn", "post", "ys", "cis", "se", "ops", "one", "edit", "testing", "xt", "affiliate", "y",
            "train", "orion", "j", "mb", "build", "developers", "pr", "s1", "edi", "nb", "ds", "pj", "trac", "ac",
            "mkt", "ci", "gate", "csc", "mailer", "kf", "www7", "golf", "canada", "imp", "gm", "bugzilla",
            "development", "nanjing", "ar", "insight", "ns0", "zz", "profile", "ns01", "seo", "gs", "aaa", "law",
            "about", "act", "mercury", "star", "sam", "parking", "apollo", "dev1", "cgi", "police", "energy", "k",
            "websphere", "weblogic", "admissions", "gd", "sl", "sk", "mc", "www35", "xf", "free", "website", "faculty",
            "bio", "bh", "earth", "india", "xh", "ph", "wm", "study", "japan", "gov", "xs", "nagios", "conf", "zeus",
            "at", "smart", "bk", "win", "rc", "tl", "cps", "ice", "pan", "ah", "bak", "team", "tool", "gl", "ideas",
            "safety", "s2", "baby", "beijing", "db1", "nz", "ie", "dr", "UN", "athena", "bd", "ceshi", "no", "up", "is",
            "cg", "iphone", "welcome", "red", "domain", "affiliates", "control", "class", "voip", "gps", "cam",
            "network", "film", "by", "fi", "track", "nt", "arc", "pluto", "jf", "sdc", "www6", "traveler", "mt", "a1",
            "telecom", "voice", "arch", "redirect", "drive", "billing", "ccs", "dh", "blue", "arts", "its", "phoenix",
            "wwwdev", "l", "cy", "webtrends", "books", "redmine", "nic", "webcam", "play", "sport", "ims", "tc", "ns02",
            "engineering", "sun", "web3", "supplier", "syslog", "mg", "o", "www36", "mirror", "products", "bill", "sa",
            "tfs", "eas", "loopback", "talk", "mp3", "foundation", "tracker", "mail4", "pk", "college", "housing", "hp",
            "uploads", "www8", "router", "board", "aws", "gy", "oa1", "green", "fl", "mac", "jm", "chemistry",
            "mailserver", "plus", "group", "kh", "ricard", "beauty", "aa", "antivirus", "repo", "cat", "discover", "pg",
            "venus", "center", "dragon", "titan", "hi", "dg", "courses", "pki", "box", "portfolio", "vod", "boss", "jl",
            "astro", "tt", "solutions", "wwws", "solr", "un", "msg", "hybrid", "la", "mtest", "picard", "ios", "sw",
            "mas", "tel", "nms", "webapp", "km", "firewall", "bank", "recruit", "tms", "www9", "wsj", "source",
            "emergency", "read", "lm", "am", "gift", "www43", "nursing", "ht", "img2", "rp", "google", "water",
            "report", "dp", "iris", "analytics", "neptune", "lady", "guide", "img1", "eshop", "ww1", "db2", "csg",
            "man", "volunteer", "webserver", "pd", "phpmyadmin", "webmaster", "count", "jt", "eis", "mj", "marketplace",
            "delta", "computer", "java", "comm", "bs", "focus", "horizon", "jg", "pdf", "guest", "upgrade", "vision",
            "leo", "lg", "monitoring", "active", "psychology", "ariel", "hl", "nano", "cb", "ces", "haosf", "oss", "hc",
            "sky", "www37", "logs", "fj", "auction", "lw", "banner", "jr", "ep", "jenkins", "webservice", "happy",
            "mail01", "tx", "gold", "eps", "app1", "translate", "cdn2", "10", "sos", "saturn", "xg", "sis", "sr",
            "espanol", "form", "sn", "resources", "py", "gz", "ap", "mantis", "vcs", "wordpress", "solar", "chinese",
            "contact", "mobil", "www41", "planet", "5", "tm", "internet", "splunk", "bug", "physics", "gsa", "studio",
            "ty", "ccc", "mta", "4", "jc", "15", "cacti", "sale", "xian", "hpc", "ww3", "singapore", "wy", "com", "ren",
            "adv", "production", "tb", "mag", "audit", "01", "mo", "w1", "jpk", "loghost", "mse", "sus", "counter",
            "eagle", "geo", "sec", "mh", "acm", "check", "elasticsearch", "bo", "hf", "adserver", "hongkong", "hot",
            "vm", "struts", "php", "air", "kj", "feed", "02", "m2", "drm", "sbc", "disk", "trip", "mr", "pics", "ping",
            "accounting", "cars", "gp", "wow", "nn", "europe", "virtual", "ba", "spider", "core", "che", "dd", "gr",
            "users", "nib", "zend", "sps", "pin", "homer", "os", "registrar", "faq", "fy", "system", "passport",
            "matrix", "el", "credit", "ea", "ta", "kk", "safe", "join", "ge", "webaccess", "lc", "movies", "qq",
            "science", "analysis", "taobao", "mx3", "moa", "flow", "payment", "creative", "echo", "ua", "mini", "sas",
            "facilities", "cdn1", "8", "gk", "wifi", "bms", "dns4", "v2", "real", "news2", "orange", "jjc", "imail",
            "ras", "src", "publications", "communications", "ecommerce", "bgs", "ns6", "people", "ro", "nexus", "www01",
            "test3", "xmpp", "france", "ipv6", "oracle", "sem", "eu", "sou", "orders", "retail", "wc", "lx", "op", "xc",
            "ares", "find", "alert", "hm", "german", "case", "nginx", "wei", "iss", "engage", "hu", "mailbox", "www14",
            "tiger", "next", "pma", "gt", "nw", "commerce", "backend", "aj", "lh", "econ", "chicago", "fang", "museum",
            "ab", "si", "wf", "advertising", "nm", "paper", "elastic", "www34", "sv", "www10", "amp", "yt", "dag", "zs",
            "www12", "ismart", "moon", "wa", "technology", "school", "www11", "ka", "widget", "ck", "pharmacy", "csr",
            "taiwan", "president", "bus", "mw", "7", "fk", "jh", "lf", "french", "server5", "mob", "ok", "wd", "2013",
            "18", "biology", "ddh", "hydra", "reader", "city", "shop2", "kc", "om", "xxx", "galaxy", "gatekeeper",
            "expo", "wg", "rm", "spanish", "drupal", "ln", "database", "9", "voicemail", "statistics", "sanguo", "pv",
            "mcs", "af", "robot", "et", "ipad", "query", "fd", "traffic", "he", "mnews", "enroll", "s3", "classic",
            "m1", "www02", "http", "cmp", "cart", "max", "17", "bf", "action", "philosophy", "att", "smg", "psych",
            "mv", "ai", "channel", "16", "mailing", "li", "was", "publish", "fun", "20", "bl", "nk", "editor",
            "external", "smtp3", "rds", "eos", "df", "med", "apex", "grad", "sap", "ko", "vpn3", "jboss", "picwww",
            "emba", "ext", "manyi", "re", "pingan", "classifieds", "03", "korea", "expert", "knowledge", "po",
            "voyager", "legal", "devel", "newton", "speed", "lj", "pi", "rz", "touch", "fa", "ics", "quiz", "alerts",
            "srm", "www15", "style", "io", "soc", "index", "vn", "sol", "11", "ws1", "a2", "abs", "healthcare",
            "economics", "athletics", "applications", "idea", "td", "www31", "kiosk", "ha", "lian", "ssc", "dir",
            "junshi", "19", "vega", "sjc", "2012", "oc", "www13", "epaper", "kt", "bw", "zj", "pad", "pass", "academic",
            "14", "akamai", "cisco", "develop", "wk", "london", "static1", "mz", "eco", "ebook", "on", "sirius",
            "pegasus", "policy", "gemini", "bca", "artemis", "line3", "aries", "yule", "fp"
        , "gaj", "dsp", "2014", "server2", "chang", "tmp", "demo2", "munin", "gjqx", "intl", "angel", "ecs",
            "mon", "hah", "helios", "config", "asset", "pulse", "rfb", "compass", "discovery", "dcs", "diamond",
            "charon",
            "eb", "procurement", "www30", "care", "msa", "bridge", "civil", "lv", "hw", "12", "fgw", "rsj", "aoe1",
            "sea", "admin2",
            "we", "wwwww", "13", "za", "gf", "ajax", "mf", "dns0", "casper", "gj", "tn", "teach", "wwwb", "pet",
            "gamma", "jump", "cds", "stores",
            "kjj", "er", "abacus", "isis", "young", "broadcast", "pool", "ec2", "www16", "esp", "al", "v2-ag", "visa",
            "advance", "wpad", "sss", "ali", "piwik", "africa", "callback", "bp", "www33", "img01", "thor", "icon",
            "allwww", "ao", "page", "zm", "graphics", "mail5", "spain", "success", "pre", "qqmail", "football",
            "express", "jcb", "noprefix", "christmas", "russian", "swt", "biotech", "verify", "vault", "printing",
            "rose", "myadmin", "dance", "wwyx", "demo1", "wwv", "today", "explore", "price", "www21", "fusion", "ld",
            "www17", "testapi", "trade", "wwwa", "wwwd", "wwxu", "caiwu", "aaron", "maths", "wwux", "apt", "aurora",
            "luna", "ww6", "www26", "error", "console", "static2", "best", "hj", "australia", "www22", "ocean", "paris",
            "xd", "mx4", "gw1", "silver", "cse", "moss", "fod", "wwvx", "soso", "iphone4s", "wwu", "ww5", "nh", "plan",
            "cdn1122", "wwvv", "193", "cbs", "chrome", "jy", "polaris", "magic", "www78", "point", "2011", "www32",
            "164", "cams", "t7", "zabbix", "koa", "dream", "zh", "helix", "adam", "sorry", "hero", "ifeng", "webgame",
            "bia", "www20", "www18", "darwin", "yahoo", "vs", "huan", "domino", "wwwh", "cpc", "base", "comic", "ww9",
            "neo", "jb", "long", "cap", "scs", "medicine", "wz", "4g", "cancer", "app2", "ips", "www-2", "match",
            "www27", "impact", "imc", "fin", "wwb", "germany", "jjw", "oas", "janus", "400", "www29", "adsl", "idm",
            "party", "ed", "cls", "hera", "led", "virus", "dss", "oma", "digi", "culture", "spark", "mx15", "amazon",
            "call", "ssp", "su", "isc", "talent", "storm", "csp", "brazil", "www24", "goto", "na", "wwxv", "yc", "ng",
            "cu", "cad", "fujian", "ws2", "zx", "zhidao", "webcdn", "omega", "apc", "az", "cme", "wwvy", "d9", "wwwf",
            "trace", "lion", "kz", "emp", "planning", "wwwc", "oem", "all", "wwyv", "wwxy", "export", "cec", "zone",
            "aps", "prism", "schedule", "fdc", "mexico", "alice", "qr", "wwvu", "il", "gopher", "swj", "quality",
            "wwuy", "lk", "dv", "odin", "tom", "qt", "chart", "russia", "cdn3", "vps3", "pilot", "wwwl", "b2c", "mmm",
            "merlin", "advantage", "triton", "aac", "lb1", "wwx", "signin", "static3", "ils", "www19", "notebook",
            "fire", "sub", "cea", "abracadabra", "np", "wlan", "line4", "bar", "smc", "tag", "wwa", "wwy", "cdc", "mcp",
            "panda", "wwwfilter", "sina", "sociology", "wwyu", "scm", "friends", "avatar", "vms", "aging", "wwuv",
            "extra", "shell", "adc", "poseidon", "fast", "wo", "ctc", "wac", "misc", "back", "spa", "v1", "te", "abel",
            "xz", "wwwv", "zt", "robin", "galileo", "iam", "ve", "wss", "wave", "2009", "wan", "author", "dhcp", "kw",
            "2010", "hercules", "img3", "test4", "agile", "www28", "messenger", "pb", "anywhere", "quote", "aas",
            "smtp4", "171", "ecom", "coop", "reseller", "honors", "www520", "guinv", "ethics", "kai", "ons", "image3",
            "king", "tibet", "ehs", "pandora", "www23", "politics", "lining", "fensike", "125125", "bme", "aba",
            "cerberus", "mzt", "company", "cts", "srv", "iso", "etc", "italy", "jx", "oasis", "tea", "images2", "bak78",
            "sds", "pds", "ece", "test5", "scan", "xn", "ais", "aim", "agora", "sme", "clubs", "www25", "das",
            "provost", "patch", "isp", "jason008", "135", "cognos", "wsc", "rainbow", "99comcn", "321", "rw", "360",
            "cma", "aq", "domains", "abraham", "baike", "wwwe", "888", "mn", "csm", "scholar", "grid", "psy", "wwwi",
            "outbound", "bak219", "common", "abragam", "vi", "homewo", "abra", "andromeda", "ui", "trans", "cluster",
            "tesla", "owl", "xy", "aero", "kangar", "trust", "jcc", "v3", "friend", "ada", "qd", "kp", "theatre",
            "oscar", "squid", "ota", "einstein", "zy", "mcu", "flight", "graphite", "wind", "187", "blackberry", "yx",
            "rec", "topaz", "m3", "bike", "challenge", "mail6", "csi", "inventory", "central", "abe", "jz", "review",
            "hospital", "lcs", "kronos", "coe", "alliance", "personal", "ti", "filter", "vista", "abrams", "bak204",
            "p2", "prime", "release", "now", "ez", "newyork", "spectrum", "download2", "quan", "pw", "yum", "carbon",
            "369", "mx11", "3d", "yanbak133", "mx5", "fish", "oms", "logo", "outreach", "adams", "byseg854", "gaia",
            "bbb", "yaho", "host2", "mx10", "sac", "api2", "sage", "template", "test6", "mu", "bamboo", "154", "wwwg",
            "summit", "mailhub", "nba", "eg", "management", "w4", "fly", "submit", "boston", "watch", "penguin",
            "application", "gitlab", "privacy", "premium", "phys", "lnmp", "wwvwv", "brain", "black", "npx", "ieee",
            "demo3", "coffee", "root", "you", "dns4512", "stmp", "adp", "houston", "weibo", "dali", "bak7", "thailand",
            "watson", "bn", "mx14", "future", "mwww", "xm", "aquarius", "hello", "advisor", "purchasing", "amber",
            "194", "xfz", "suppliers", "cntv", "stars", "try", "industry", "itc", "dns4527", "cs2", "ia", "adventure",
            "lu", "kd", "warehouse", "aag", "cee", "cdn4", "ebs", "budget", "cctv", "a01", "cai", "europa", "panel",
            "ias", "nova", "pay3", "agenda", "chi", "lotus", "falcon", "fashion", "v9", "url", "img0", "apis", "cafe",
            "text", "wwvvv", "ibm", "deploy", "bounce", "129", "platform", "snap", "im2", "uranus", "buzz", "apache",
            "fw1", "vendors", "aal", "holiday", "toolbox", "mmc", "austin", "tick", "fh", "s4", "bob", "berlin",
            "hyperion", "beacon", "bao", "cosmos", "tele", "do", "dds", "c1", "msn", "aw", "image1", "t2", "dns2138",
            "3w", "2008", "wedding", "cv", "dolphin", "168", "mai", "ews", "sugar", "merchant", "sqlserver", "232",
            "ucenter", "nat", "nav", "mails", "antares", "px", "intern", "mes", "f5", "dvd", "park", "html", "beian",
            "crs", "wall", "private", "ak", "tst", "platinum", "derek", "ux", "fg", "cmc", "dbs", "shop1", "cards",
            "d1", "wizard", "167", "parts", "vpn01", "server3", "lq", "asc", "4050", "mq", "netmon", "3com", "aqua",
            "t1", "dell", "zzz", "hades", "moe", "psp", "pss", "radar", "shs", "camera", "oa2", "ev", "isa", "yd",
            "ts1", "big", "daily", "animal", "admin1", "waimai", "snow", "smail", "tourism", "quantum", "demos", "cst",
            "hope", "ws3", "ccm", "medusa", "yl", "8u", "big5", "rx", "rr", "cns", "mss", "comet", "alt", "miami",
            "atlantis", "exmail", "mirrors", "dna", "key", "kg", "sta", "ars", "discuss", "gms", "none", "cs1", "img02",
            "score", "ii", "wsb", "172", "epc", "interactive", "san", "outlet", "coach", "keyserver", "vtc", "scp",
            "profiles", "ceres", "icp", "ppp", "crystal", "lynx", "nf", "rsa", "quest", "player", "notify", "rf", "160",
            "geography", "abraxas", "collection", "clock", "jia", "vp", "franklin", "wenwen", "bobo", "sakai", "women",
            "yuan", "batman", "nemo", "zjj", "ding", "ucc", "xcb", "pim", "mk", "geology", "c2", "4006", "oauth",
            "mango", "jazz", "metric", "alex", "turkey", "flv", "k2", "shadow", "news1", "s5", "ccb", "forest",
            "abbott", "x2", "i2", "sjb", "unix", "maple", "navigator", "xinjiang", "ke", "yj", "novel", "cce", "euler",
            "ups", "eval", "malaysia", "sci", "skb", "athens", "cygnus", "image2", "thunder", "techsupport", "qz",
            "moban", "medical", "asm", "ruby", "v7", "api1", "d2", "exp", "model", "gq", "ghost", "poc", "sigma",
            "wine", "resume", "sjz", "bear", "fox", "bell", "kiwi", "breeze", "metro", "dps", "dorm", "host1", "jerry",
            "b1", "apm", "cricket", "encore", "ttt", "esb", "jaguar", "cip", "aahl", "login2", "kerberos", "mx13",
            "dodo", "mds", "sxy", "sphinx", "diy", "run", "e11", "t3", "i1", "xj", "cube", "dn", "msp", "crc",
            "aardvark", "brown", "castor", "aardwolf", "hambur", "ylc", "agency", "baoming", "w7", "lucky", "cyber",
            "ben", "1111", "apitest", "wuyw", "spring", "xia", "climate", "dept", "testsite", "lz", "argentina", "asa",
            "jsw", "c3", "swf", "transport", "aachen", "mail7", "bx", "puma", "an", "mbs", "trs", "bing", "wcs",
            "extension", "aahz", "386", "jilin", "trial", "virgo", "raven", "s12", "nx", "drc", "arizona", "nd", "pdm",
            "162", "data1", "sitemap", "yw", "epic", "lin", "aallan", "muse", "som", "loki", "c4", "zk", "rank", "pac",
            "gx", "github", "dynamic", "lgb", "ll", "advice", "maint", "lead", "ses", "atm", "184", "if", "super",
            "pat", "pmp", "tlc", "host4", "365", "psa", "ad2", "atlanta", "esd", "ceo", "bsc", "du", "msc", "attach",
            "w5", "download1", "openapi", "vss", "bis", "oak", "cit", "aaguirre", "libra", "xyz", "rich", "stargate",
            "genome", "mail10", "light", "mod", "pod", "genesis", "seminar", "abcd", "qinghai", "texas", "mam", "iron",
            "aberdeen", "gauss", "indigo", "tts", "cmt", "emc", "eric", "activity", "mil", "wu", "lao", "peixun",
            "yunfu", "assist", "robotics", "sydney", "raptor", "p3", "zero", "rabbit", "eol", "hawk", "ax", "ccp",
            "netlab", "juno", "aapo", "abramson", "suzhou", "vvvww", "sep", "hudson", "shenzhen", "v5", "shanxi", "e10",
            "nv", "va", "washington", "sdk", "todo", "mark", "nike", "out", "imgs", "wvux", "jade", "qb", "r1", "bbc",
            "v4", "192", "mbox", "lan", "opinion", "hebei", "wap2", "wuxw", "cop", "attachments", "img4", "zr",
            "maxwell", "hhh", "aab", "lisa", "turing", "nanke", "seattle", "clothes", "wuvx", "or", "buffalo", "avalon",
            "subversion", "nntp", "banking", "zen", "urchin", "interface", "vps2", "esales", "ad1", "yn", "zc", "l2",
            "p2p", "guangdong", "plant", "maillist", "dls", "aage", "vps1", "tcs", "sell", "pz", "cca", "tianjin", "hx",
            "gaokao", "fantasy", "fred", "larry", "aadams", "h5", "dl1", "eye", "skynet", "mgt", "i4", "114", "taurus",
            "more", "token", "mps", "bulletin", "broker", "img7", "album", "svc", "ict", "pacific", "p4", "m4", "gems",
            "showcase", "f1", "cn2", "qhd", "xing", "windows", "opal", "111", "minerva", "aes", "177", "sample", "tim",
            "logos", "bigbrother", "zhao", "juniper", "9933", "godaddy", "dnstest", "farm", "jordan", "125", "166",
            "p1", "pack", "djh", "aragorn", "general", "qh", "img6", "imaging", "cobra", "smtp5", "mapi", "ningxia",
            "smtp10", "img5", "666", "award", "sga", "h3", "bdf", "chaos", "altair", "abo", "t5", "xk", "host3", "hal",
            "xq", "g7", "bbs2", "ring", "ur", "fishing", "qy", "humanities", "k3", "jss", "stc", "sunshine", "cie",
            "spock", "bbs1", "f2", "198", "court", "aims", "jcj", "lamp", "yz", "777", "bts", "ebh", "callisto", "t4",
            "elite", "ff", "r2", "offline", "vancouver", "setup", "mov", "zwj", "snoopy", "tokyo", "yh", "xiao", "to",
            "white", "wj", "148", "vl", "ldj", "perseus", "delphi", "1234", "e7", "bq", "chaxun", "fff", "mimi", "eva",
            "tss", "cn1", "mail9", "youjizz", "ibs", "pdc", "phobos", "tec", "bolg", "wvw", "xmail", "nemesis", "ipm",
            "yulanyou", "wechat", "jiangxi", "update2", "good", "ford", "land", "message", "seller", "ol", "micro",
            "xiu", "helper", "qm", "artist", "spf", "agri", "stem", "hc5", "147", "uni", "scc", "sex", "omni", "aasa",
            "aca", "logon", "a3", "trash", "fanli", "consulting", "lucy", "marvin", "yuyue", "181", "lis", "west",
            "ykt", "zixun", "um", "fortune", "m5", "img8", "qing", "story", "sim", "mft", "sat", "aap", "v6", "js1",
            "hainan", "tablet", "dmc", "aad", "xen", "trinity", "child", "install", "ib", "two", "login1", "s01",
            "purchase", "osiris", "acsvax", "800", "ditu", "smtp7", "chicken", "photon", "allen", "q1", "999", "ivr",
            "abby", "jie", "mail8", "picture", "david", "mgr", "casa", "socrates", "aacse", "mail12", "east", "jasper",
            "gi", "cname", "dba", "purple", "agnes", "topic", "baidu2014", "zt2", "124", "hubei", "tongji", "000",
            "transit", "person", "stone", "ip2", "n2", "rh", "zhaopin", "dcc", "smp", "port", "odyssey", "mail-4",
            "ipod", "ay", "anhui", "tap", "finaid", "rap", "drp", "e3", "at820", "bailefang", "vegas", "eclipse",
            "byby", "wuwv", "182", "mx6", "di", "ei", "smile", "camel", "gansu", "sign",
            "u1", "157", "nokia", "nfs", "soap", "b2", "wap1", "fuke", "test123", "010", "t6", "211", "e1", "cgs",
            "supply", "djj", "hlj",
            "a10", "custom", "argon", "titanium", "jingjia", "71", "bei", "197", "guangxi", "dot", "tf", "gandalf",
            "iq", "ets", "biochem",
            "lobby", "task", "wuxv", "dq", "tips", "sft", "psc", "think", "reach", "mx7", "dai", "tcm", "lyg",
            "daohang", "wuxy", "shu", "pptp",
            "neon", "file2", "1314", "uu", "charlotte", "ebay", "dean", "tuku", "columbus", "feng", "liu", "xin",
            "imgcdn", "euro", "tomcat"
        , "turbine", "launch", "app01", "abalone", "yb", "jxc", "pinpai", "wvxy", "99", "ye", "samsung", "fu", "cpe",
            "a02", "g1", "w9", "c5"
        , "wuwy", "149", "bee", "dtm", "ash", "guangzhou", "bach", "xray", "vb", "synergy", "s7", "metis", "chanel",
            "zeta", "zn", "eureka",
            "phantom", "sogou", "cha", "wuhan", "shouji", "depot", "ddd", "acp", "wuv", "mgame", "dao", "chef", "eee",
            "sbs", "fuck", "d3", "555"
        , "988", "ha5", "hua", "proteus", "75", "tps", "zhu", "vis", "rl", "zf", "zg", "qs", "cmcc", "95", "a12",
            "wuwx", "hunan", "qj", "ya",
            "niu", "sfs", "honey", "joe", "viper", "cobalt", "cpa", "elvis", "202", "cba", "amd", "ait", "dove", "yang",
            "smtp6", "21", "100",
            "vortex", "vv", "laser", "hai", "abricot", "michaelyu", "404", "skin", "other", "tree", "chess", "dl2",
            "m6", "shoes", "rome", "qg"
        , "gn", "ecc", "clarity", "emma", "monkey", "129979", "pix", "amsterdam", "mir", "acer", "rest", "systems",
            "esl", "smtp9", "dispatch"
        , "lyris", "abell", "wuxi", "kehu", "piao", "gdsvr", "miao", "mail15", "gu", "srs", "olive", "director",
            "registry", "yoda", "sprout",
            "b5", "ut", "joke", "vnet", "broadband", "dam", "117", "guanli", "fanyi", "flower", "g1i8", "hg3", "wxtest",
            "john", "ku", "italian",
            "tmail", "biomed", "gem", "his", "alcor", "bd123002", "kaoshi"]
    #
    def mk(self,*k):
        res = set().union(set(self.dist))
        for x in k:
            if type(x) == type(set()):
                res = res.union(x)
            if type(x) == type(list()):
                res = res.union(set(x))

        return set(res)

################################################################
## TH
import threading
class rt:
    threads = []
    threadcc = 0
    remain = False
    cousor = 0
    limi = 0
    lc = 0
    silent = False


    def thstart(self,gap=0,timel=0,wait=0):
        i=0
        lim = 0
        for thx in self.threads:
            thx.setDaemon(True)
            thx.start()

            if i >= gap:
                time.sleep(timel)
            else:
                i += 1
            lim+=1
            if lim == self.limi and self.limi != 0:
                while self.lc<self.limi:
                    # print(self.limi)
                    # print(self.lc)
                    pass
                self.lc = 0
                lim = 0
        if wait != 0:
            time.sleep(wait)
        else:
            while self.threadcc != 0:
                pass

        self.threads.clear()

    def thappend(self,x,tp):
        self.threads.append(threading.Thread(target=x, args=tp))
        self.threadcc += 1

    def thappendm(self,x,tp):
        self.threads.append(threading.Thread(target=x, kwargs=tp))
        self.threadcc += 1

    def cop(self,f,**k):
        try:
                f(**k)
        except Exception as e:
                if self.silent:
                    print("\r[E][{}]".format(e),end="")
                else:
                    print("[E][{}]".format(e))
        finally:
                if self.remain == True:
                    pass
                self.threadcc -=1
                self.lc += 1

        return f

    def thappcop(self,f,k):
        arg = {'f': f}
        arg.update(k)
        self.thappendm(self.cop,arg)

def execm(ec, dict):
    tpw = rt()
    tpw.thappcop(ec, dict)
    tpw.thstart(wait=1)

################################################################
##Str porc
def file2li(f,en = "utf8"):
    sett = set()
    ff = open(f,"r",encoding=en)
    for x in ff.readlines():
        sett.add(x.strip())
    ff.close()
    return sett

def loaddic(dir = "./dict/"):
    import os
    fi = os.scandir(dir)
    dic = dictionary()
    res = []
    for x in fi:
        res += dic.mk(file2li("./dict/" + x.name), res)
    return set(res)

def limit(obj,inp):
    return inp%len(obj)

def readfile(file):
    with open(file,"r") as f:
        return f.read()

def wfile(path,st):
    with open(path,"a") as f:
        f.write(st)
        f.close()

def li2str(s = [],sep = ",",pos = True):
    res = ""
    for x in s:
        if not pos:
            res += x + sep
        if pos:
            res += sep + x
    res+="\n"
    return res

def tu2set(s,sets):
    for x in s:
        sets.add(x)
    return sets

def Md5(Str = ""):
    import hashlib
    return hashlib.md5(Str.encode('utf8')).hexdigest()

def base64en(Str):
    import base64
    return base64.b64encode(Str.encode())
################################################################
##DNS
import sys,socket
def Dns_plain(domain):

    try:
        res = socket.gethostbyname(domain)
        raw = res
        return tuple(res), raw
    except Exception as e:
        raise Exception(str(e)+":"+domain)

def Dns_Query_addr(domain,serverlist = ["114.114.114.114"]):
    A = dns.resolver.resolve(domain)
    A.nameservers = serverlist
    A.timeout = 15
    A.lifetime = 15
    res = set()
    for i in A.response.answer:
        for j in i.items:
            if j.rdtype == 1:
                res.add(j.address)
    raw = res
    return tuple(list(res)),raw

################################################################
##DOmain
class scanDomain:
    tmpset = set()
    allurls = []
    rd = ramdd()
    def __init__(self):
        dic = dictionary()
        self.scanli = dic.mk(dic.dist, loaddic())

    def lifile(self):
        self.tmpset.update(loaddic())

    def cfgli(self,jsons):
        tempset = set()
        jsono = json.loads(jsons)
        rd = jsono["rd"]
        for x in rd.keys():
            k = int(x)
            v = rd.get(x)
            tempset.union(self.rd.randnumlist(k,v))
        self.tmpset.union(tempset)
        tempset.clear()
        rc = jsono["rc"]
        rck = list(rc.keys())[0]
        print(rck)
        rcv = rc.get(rck)
        for x in rcv:
            for xx in range(int(rck)):
                tempset.add(self.rd.ramdschar(x))

    def sclit(self,url = ""):
        res = set()
        self.cfgli(readfile("./gen.json"))
        self.lifile()
        self.allurls = list(self.tmpset)
        bit = url.count("{")
        let = len(self.allurls)
        clc = defclock(bit, let)
        for x in range(clc.forl):
            clc.tick()
            bil = url
            for xx in range(bit):
                bil = bil.replace("{"+str(xx)+"}",str(self.allurls[limit(self.allurls,clc.li[xx])]))
            print("\r{}/{}".format(str(clc.li[0]),str(clc.li[-1])),end="")
            res.add(bil)
        print("========ok========")
        return res

def logdomain(dic,domain,cmpset = {},rdomain = {}):
    try:
        tmp = domain.split(".")
        ep = tmp = tmp[limit(tmp, 1):]
        tmp = li2str(tmp, ".")
        if  rdomain.get(tmp) != None:
            print("[exit:domain]")
            return
        if burpmode == 1:
            res, raw = Dns_Query_addr(domain, serverlist=servlist)
        elif burpmode == 2:
            res, raw = Dns_plain(domain)
        if len(ep) >= 3:
            if cmpset.get(tuple(res)) != None:
                rdomain[ep] = ""
                return
        if cmpset.get(tuple(res)) != None:
            return
        if dic.get(domain) == None:
            cmpset[tuple(res)] = ""
            dic[domain] = set()
        try:
            dic[domain].update(raw)
        except Exception as e:
            raise Exception(e)
    except Exception as e:
        print("[E][{}]".format(e))

def burp(domain):
    domains = dict()
    doms = scanDomain().sclit(domain)
    domlen = len(doms)
    Rt = rt()
    Rt.silent = False
    cmpset = dict()
    rdset = dict()
    j = json.loads(open("perfom.json").read())
    i = 0
    sta = False
    for x in range(domlen):
        don = doms.pop()
        Rt.thappcop(logdomain,{"domain":don,"dic":domains,"cmpset":cmpset,"rdomain":rdset})

        if i == j["th"]:
            Rt.thstart()
            i = 0
        if len(doms)<1:
            Rt.thstart()
            i = 0
        i += 1
        proc_monitor(x,domlen)
    doms.clear()

    return domains

def proc_monitor(a,b):
    percent = str(int((a / b) * 100))
    print("[{}/{}:{}%]".format(a, b,percent))

################################################################

i = 0
with open("./targs.txt","r") as f:
    for x in f.readlines():
        res = burp(x.strip())
        with open("./res/{}.txt".format(
                x.replace("{","").
                        replace("}","").
                        replace(":","").
                        replace(".","_").
                        strip()
                ), "a") as sf:
            for x in res:
                tres = li2str([x]+list(res.get(x)))
                print(tres)
                sf.write(tres)
            sf.close()
            res.clear()
        i+=1




