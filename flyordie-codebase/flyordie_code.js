// how does the game load and url.

//local push

TITLE_CHECKERS = "Checkers";
TITLE_CHECKERSBULLET = "Bullet Checkers";


! 

else if (game.indexOf('Checkers') == 0) {
        CODE_RELEASE = "130802uc";
        DATA_RELEASE = "130802";
        PATH = "checkers";
        JNLP_NAME = "Checkers";
        H5 = {
                CODE_SIZE: 466278,
                CODE_PAR: "氽ꄧ㗲᡽鸜빅侜棖",
                CODE_RELEASE: "181029",
                DATA_RELEASE: "180513"
        };
var ARCHIVE = CODE_RELEASE + "/load.zip," + CODE_RELEASE + "/code.zip";
var LOADCODE = CODE_RELEASE + "/code.zip";
var DROOT = "http://" + "www.flyordie.com" + "/games/deploy/";
if (JNLP) {
        DHOME = DROOT + PATH + '/';
        JARCHIVE = CODE_RELEASE + "/load.jar";
        if (JNLP < 3)
                JARCHIVE += "," + CODE_RELEASE + "/code.jar";
        AP('server', HOST);
}
if (!GAMEICON)
        GAMEICON = "../images/icon_" + PATH + ".png";
var CB = new Object();
CB.CODEBASE = "http://" + HOST + "/games/cb";
CB.ARCHIVE = "111122" + "/cb.jar";
CB.CODE = "cb";
if (MODE == 'sp')
        PBGND = DROOT + "images/pbgnd_" + (IBGND || PATH) + ".jpg";
if (H5)
        H5.T.IBGND = DROOT + "images/ibgnd_" + (IBGND || PATH) + ".t.jpg";
IBGND = DROOT + "images/ibgnd_" + (IBGND || PATH) + (".ar.fa".indexOf("." + LANG.substring(0, 2)) >= 0 && (PATH == 'tanx' || IBGND == 'board' || IBGND == 'chess3' || IBGND == 'billiards') ? '.rtl' : '')
+ (LOWRES && MODE != 'sp' ? '.y' : '') + ".jpg";
LOGO = (GAMELOGO || SITELOGO).split(',')[0];
if (FAVICON == '?')
        FAVICON = PATH;
var LGV;
function loadGame(v) {
        LGV = v || 0;
        document.write('<script id="fodj" src="' + HOME + 'games.jhtm?695" charset="UTF-8"></script>');
}
var _GAME_JS = 503;
//-->





