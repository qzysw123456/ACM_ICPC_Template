from fractions import Fraction

N = 32

def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    return c

def interpolate(values):
    coefficient = [0] * len(values)
    for xi, yi in values:
        constant, polynomial = Fraction(yi), [1]
        for xj, yj in values:
            if xi != xj:
                constant /= (xi - xj)
                polynomial = multiply(polynomial, [-xj, 1])
        for k, v in enumerate(polynomial):
            coefficient[k] += constant * v
    return coefficient

def precompute(n):
    ways = [[0] * (2 * n) for _ in xrange(n)]
    ways[0] = [1] * (2 * n)
    for i in xrange(1, n):
        for j in xrange(i, 2 * n):
            ways[i][j] = ways[i][j - 1] + ways[i - 1][j - 1] * j
    result = [0] * (2 * n)
    for i in xrange(n):
        ret = interpolate(list(enumerate(ways[i]))[:2 * i + 1])
        for k, v in enumerate(ret):
            result[k] += v * pow(2, i)
    return result

def evaluate(n):
    result = 0
    for i in reversed(xrange(len(COFFICIENT))):
        result *= n
        result += COFFICIENT[i]
    return int(result) % pow(2, N)

def cal_exp(n):
    result = 0
    while n > 0:
        n /= 2
        result += n
    return result

def inverse(a):
    return pow(a, pow(2, N - 1) - 1, pow(2, N))

def no2_product(n): # 1 * 2 * ... * n  no 2
    if n <= 1:
        return 1
    return no2_product(n / 2) * evaluate((n - 1) / 2) % pow(2, N)

def binom(n, k):
    exp = cal_exp(n) - cal_exp(k) - cal_exp(n - k)
    ret = pow(2, exp)
    ret *= no2_product(n)
    ret *= inverse(no2_product(k))
    ret *= inverse(no2_product(n - k))
    return ret % pow(2, N)

def main():
    n, k = map(int, raw_input().split())
    print binom(n, k)

# {{{
COFFICIENT = [Fraction(1, 1), Fraction(-8727115113629814390855506612, 410237366175), Fraction(1549245699873139152705021816020342, 2509513132751625), Fraction(80187176705620854861940258672494357938, 704332503403734830625), Fraction(-937163558057018715011119529493122509006, 477128470047691336875), Fraction(-276559073871743421609480222121906629129664, 2254432020975341566734375), Fraction(196666578669000175387817742697617636876742, 78826294439697257578125), Fraction(-1374420896679694009562528075933532904559588, 46113382247222895683203125), Fraction(-127966678982868833107000060765524007463372, 75719839486408695703125), Fraction(248254411351877228604171294631383620601284, 2044435666133034783984375), Fraction(576459491397865463028077091390865080011009, 817774266453213913593750), Fraction(-23105550266959133323758960271750834297428037, 257598893932762382782031250), Fraction(-231448801656785334673650125621403695412238519, 1177594943692628035575000000), Fraction(1843757125718999633769495032409991606357317419, 51004580998686951790842187500), Fraction(3976486187745570348117382373466655004900422061, 103628355044951267130600000000), Fraction(-32032048823002306896020364988457407872872451107, 3357558703456421055031440000000), Fraction(-260639573178491799762897178703233759848725500957, 48837217504820669891366400000000), Fraction(11730843932861322002016522695121388273979342861, 6574240817956628639222400000000), Fraction(3675006770295454051274278031384666700388606141, 7122094219453014359157600000000), Fraction(-1560661562080000567109542357733145409123089977, 6330750417291568319251200000000), Fraction(-16891839428775752983336174407595851813921509, 566228608751543998740480000000), Fraction(7769548983979245838761862601430393978579343, 303336754688327142182400000000), Fraction(-25984660920246516498301548747944700483173, 3397371652509263992442880000000), Fraction(-29875195666502405207355831496583972646730093643, 15041862991484766326540851200000000), Fraction(11361209126041113985087698963166572204109433887, 53482179525279169161034137600000000), Fraction(160852083262850786926942852961631807564050563, 1485616097924421365584281600000000), Fraction(-53617617567048409476730407335311653589982183, 2083721280205681915364966400000000), Fraction(-11181399613726698357271047120001216575827, 3572093623209740426339942400000), Fraction(12849466134833449535973312831816900844649381, 7144187246419480852679884800000000), Fraction(-208358476634711267784588271333859692072435019, 2537972519290520572914529075200000000), Fraction(-7849135566380345870846746143669399403921799, 104121949509354690170852474880000000), Fraction(13053143616941019596778871975585924043463679, 863398058688681895861184102400000000), Fraction(121286658947786689687843357964063256744547, 138760402289252447549118873600000000), Fraction(-15665383217307561260223543974705331693610243, 20185390765669213186328965939200000000), Fraction(9233227253316692385326079535831469536553, 87653681984915938154033971200000000), Fraction(406473738329211599133388055957333264079403, 44668316339513162083295711723520000000), Fraction(-164738725716073855671164044067829939337, 29172097922879546815109529600000000), Fraction(7864835947089773678495150485185266519, 8643584569742087945217638400000000), Fraction(-50624775599880639004059938228028269, 2083721280205681915364966400000000), Fraction(-319272296614025341193791898213866039, 14288374492838961705359769600000000), Fraction(16088972590803129960845870967317543, 2500465536246818298437959680000000), Fraction(-111064383872325018831549906201257239, 100018621449872731937518387200000000), Fraction(8151630563469270486418871443927, 56371203715709269207941120000000), Fraction(-2459665393967869585276445586737, 161060582044883626308403200000000), Fraction(5390739077347018095861141817631, 3986249405610869751132979200000000), Fraction(-63531738162252087293261118611, 621233673601693987189555200000000), Fraction(333896858694663714335177290237, 50009310724936365968759193600000000), Fraction(-37885295014758857307863998831, 100018621449872731937518387200000000), Fraction(3124095392585044344513901, 166697702416454553229197312000000), Fraction(-7347146703411243041689, 9071983804977118543085568000000), Fraction(16979742819649882198307, 555659008054848510763991040000000), Fraction(-203024597295271884973, 202057821110854003914178560000000), Fraction(531374213693177489, 18521966935161617025466368000000), Fraction(-47650022868363169, 67352607036951334638059520000000), Fraction(51297443339647, 3429993876881780930641920000000), Fraction(-3154893759859, 11759979006451820333629440000000), Fraction(41446160713, 10289981630645342791925760000000), Fraction(-272596637, 5487990203010849489027072000000), Fraction(97473967, 198939644859143293977231360000000), Fraction(-328631, 88417619937397019545436160000000), Fraction(89, 4372299887014138329169920000000), Fraction(-1, 13960676832220582033489920000000), Fraction(1, 8222838654177922817725562880000000), 0]
# }}}
main()
