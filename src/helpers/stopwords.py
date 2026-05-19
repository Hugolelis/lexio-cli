from pathlib import Path

STOP_WORDS_EN_CONJUNCTIONS_CONNECTIVES = {
    "and", "or", "but", "nor", "yet", "so", "for", "however", "therefore",
    "thus", "hence", "moreover", "furthermore", "nevertheless", "nonetheless",
    "although", "though", "while", "whereas", "whereby", "meanwhile",
    "consequently", "accordingly", "otherwise", "else", "still", "also",
    "besides", "additionally", "likewise", "similarly", "conversely",
    "instead", "rather", "notwithstanding", "regardless", "anyway",
    "anyhow", "yet", "even", "just", "only", "merely", "simply",
}

STOP_WORDS_EN_ARTICLES_PRONOUNS = {
    "a", "an", "the", "i", "me", "my", "mine", "we", "us", "our", "ours",
    "you", "your", "yours", "he", "him", "his", "she", "her", "hers",
    "it", "its", "they", "them", "their", "theirs", "one", "ones",
    "myself", "yourself", "himself", "herself", "itself", "ourselves",
    "yourselves", "themselves", "who", "whom", "whose", "which", "what",
    "that", "this", "these", "those", "somebody", "someone", "something",
    "anybody", "anyone", "anything", "nobody", "nothing", "everybody",
    "everyone", "everything",
}

STOP_WORDS_EN_PREPOSITIONS = {
    "in", "on", "at", "to", "for", "of", "with", "by", "from", "into",
    "through", "during", "before", "after", "above", "below", "between",
    "under", "again", "further", "then", "once", "here", "there", "about",
    "against", "because", "until", "while", "up", "out", "off", "over",
    "down", "around", "across", "along", "among", "within", "without",
    "upon", "toward", "towards", "beside", "beyond", "since", "via",
    "per", "plus", "minus", "versus",
}

STOP_WORDS_EN_VERBS_AUXILIARY = {
    "is", "are", "was", "were", "be", "been", "being", "am",
    "have", "has", "had", "do", "does", "did", "will", "would",
    "could", "should", "may", "might", "shall", "can", "need",
    "dare", "ought", "used", "must", "let", "make", "go", "come",
    "get", "give", "take", "know", "think", "see", "say", "tell",
    "want", "use", "find", "put", "mean", "keep", "leave", "seem",
    "become", "begin", "show", "hear", "run", "move", "live",
    "believe", "bring", "happen", "write", "provide", "sit", "stand",
    "lose", "pay", "meet", "include", "continue", "set", "learn",
    "change", "lead", "understand", "watch", "follow", "stop",
    "create", "speak", "read", "allow", "add", "spend", "grow",
    "open", "walk", "win", "offer", "remember", "love", "consider",
    "appear", "buy", "wait", "serve", "die", "send", "expect",
    "build", "stay", "fall", "cut", "reach", "kill", "remain",
}

STOP_WORDS_EN_ADVERBS_OTHERS = {
    "not", "no", "very", "too", "so", "as", "if", "than", "when",
    "where", "why", "how", "all", "each", "every", "both", "few",
    "more", "most", "other", "some", "such", "only", "own", "same",
    "now", "then", "here", "there", "always", "never", "often",
    "sometimes", "usually", "already", "yet", "still", "even",
    "just", "quite", "rather", "almost", "enough", "well", "back",
    "much", "many", "any", "also", "ever", "really", "actually",
    "probably", "perhaps", "maybe", "sure", "certainly", "definitely",
    "exactly", "especially", "generally", "mainly", "mostly", "nearly",
    "originally", "particularly", "recently", "relatively", "seriously",
    "significantly", "somewhat", "specifically", "suddenly", "together",
    "truly", "typically", "ultimately", "unfortunately", "usually",
    "various", "variously", "widely",
}

STOP_WORDS_PT = {
    "a", "o", "os", "as", "um", "uma", "uns", "umas",
    "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas",
    "por", "para", "com", "sem", "sob", "sobre", "ante", "apos",
    "desde", "entre", "contra", "perante",
    "e", "ou", "mas", "porem", "porém", "contudo", "todavia", "no entanto",
    "entretanto", "logo", "pois", "porque", "porquanto", "como", "quando",
    "que", "se", "caso", "embora", "conquanto", "apesar", "enquanto",
    "assim", "ja", "já", "ainda", "sempre", "nunca", "tudo", "nada",
    "algo", "tambem", "também", "so", "só", "muito", "mais", "menos",
    "bem", "mal", "quase", "apenas", "sozinho", "bastante",
    "eu", "me", "mim", "comigo", "tu", "te", "ti", "contigo",
    "ele", "ela", "eles", "elas", "nos", "nosso", "nossa", "nossos", "nossas",
    "vos", "vosso", "vossa", "vossos", "vossas", "lhe", "lhes",
    "este", "esta", "estes", "estas", "esse", "essa", "esses", "essas",
    "isto", "isso", "aquilo", "aquele", "aquela", "aqueles", "aquelas",
    "qual", "quais", "quem", "cujo", "cuja", "cujos", "cujas",
    "onde", "aonde", "donde",
    "seu", "sua", "seus", "suas", "meu", "minha", "teu", "tua",
    "nao", "não", "nem", "sim", "tal", "tanto", "tanta", "tantos", "tantas",
    "cada", "todo", "toda", "todos", "todas", "qualquer", "quaisquer",
    "algum", "alguma", "alguns", "algumas", "nenhum", "nenhuma",
    "outro", "outra", "outros", "outras", "mesmo", "mesma",
    "proprio", "próprio", "propria", "própria",
    "ser", "estar", "ter", "haver", "fazer", "ir", "vir", "poder",
    "dever", "querer", "saber", "parecer", "ficar", "passar",
    "chegar", "entrar", "sair", "subir", "descer", "levar", "trazer",
    "dar", "dizer", "falar", "ouvir", "ver", "olhar", "sentir",
    "achar", "pensar", "acreditar", "esperar", "tentar", "conseguir",
    "precisar", "gostar", "amar", "odiar", "pedir", "procurar",
    "encontrar", "perder", "ganhar", "pagar", "custar", "valer",
    "existir", "viver", "morrer", "nascer", "crescer", "cair",
    "levantar", "abrir", "fechar", "colocar", "tirar", "puxar",
    "empurrar", "segurar", "tocar", "chamar", "perguntar", "responder",
    "explicar", "mostrar", "escrever", "ler", "estudar", "aprender",
    "ensinar", "trabalhar", "descansar", "dormir", "acordar",
    "comer", "beber", "cozinhar", "limpar", "lavar", "secar",
    "jogar", "brincar", "dançar", "cantar", "correr", "andar",
    "pular", "nadar", "dirigir", "viajar", "voltar", "ficar",
    "de", "que", "e", "do", "da", "em", "um", "para", "com", "nao",
    "uma", "nos", "por", "mais", "se", "ja", "muito", "ha", "ele",
    "tua", "teu", "o", "eu", "seu", "ela", "tem", "qual", "voce",
    "isso", "isto", "este", "essa", "este", "esse", "aquilo",
    "aquele", "aquela", "aqueles", "aquelas",
}

STOP_WORDS = (
    STOP_WORDS_EN_CONJUNCTIONS_CONNECTIVES
    | STOP_WORDS_EN_ARTICLES_PRONOUNS
    | STOP_WORDS_EN_PREPOSITIONS
    | STOP_WORDS_EN_VERBS_AUXILIARY
    | STOP_WORDS_EN_ADVERBS_OTHERS
    | STOP_WORDS_PT
)

CUSTOM_STOPWORDS_PATH = Path.home() / ".lexio" / "stopwords.txt"


_cached_custom_stopwords: set[str] | None = None
_cached_all_stopwords: set[str] | None = None


def _load_custom_stopwords() -> set[str]:
    global _cached_custom_stopwords
    if _cached_custom_stopwords is not None:
        return _cached_custom_stopwords
    if not CUSTOM_STOPWORDS_PATH.exists():
        _cached_custom_stopwords = set()
        return _cached_custom_stopwords
    try:
        words = CUSTOM_STOPWORDS_PATH.read_text(encoding="utf-8").splitlines()
        _cached_custom_stopwords = {w.strip().lower() for w in words if w.strip() and not w.startswith("#")}
    except Exception:
        _cached_custom_stopwords = set()
    return _cached_custom_stopwords


def get_all_stopwords() -> set[str]:
    global _cached_all_stopwords
    if _cached_all_stopwords is not None:
        return _cached_all_stopwords
    _cached_all_stopwords = STOP_WORDS | _load_custom_stopwords()
    return _cached_all_stopwords


def invalidate_cache() -> None:
    global _cached_custom_stopwords, _cached_all_stopwords
    _cached_custom_stopwords = None
    _cached_all_stopwords = None


def is_stopword(word: str) -> bool:
    return word.lower() in get_all_stopwords()


def filter_stopwords(words: list[str]) -> list[str]:
    sw = get_all_stopwords()
    return [w for w in words if w not in sw]
