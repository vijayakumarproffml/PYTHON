class GRAPH():
    # vertex, adjecent vertex tellathaum print pannrathu oru idam thevaipadum,athuku tha intha self.graph ndra variable
    #inga dictionary ah store panrom,because dictionay form la panna easy ah irukum A(vertex):[B(ithu adjecent vertex)]
    # inga values ah list crate panni athula store panna porom
    def __init__(self):
        self.graph={} # format for example{A(vertex(key)):[B(adjecent verex(value))]}

    # vertex add panna porom

    def addvertex(self,vertex):
        # inga same vertax add panna koodathu, dictionary la duplicate values accept pannathu
        # ipo enter aagura vertex already ilena keela iruka process ah pannu ilena else la irukuratha pannu
        if vertex not in self.graph:
            # same vertex ah ilena vetex ah self.graph ku assaingn pannu
            # intha function la store aagura vertex ah graph la podaporom
            # vertwx ah key ah pass panrom
            self.graph[vertex]=[]
            # ipothaiku values store panrathuku empty list create panrom
            # forthcomming la vetex ah connect pannum bothu itha call panikalam
        else:
            print("vertex already exists")
        # itha mudichathum vertex ku value kudukanum fun calling moolama

    # ipo EDGES create panna porom
    # rendu vertex ku idaila tha edge create aagum so vertex1 and vertex 2nu kudukalam
    def addedges(sel,vertex1,vertex2,isDirected=False): # vertex1= A,vertex2= B
        '''ipo vertex create pannamalaye edges make panna try panna namma accept panna koodathu, error varum
        # athuku oru condition make pannanum
        # itha error varama thaduka marubadium rendu vertax ah add pannanum
        # inga add panratha la problem varathu because mela iruka condition error varama pathukum, inga same vertex 
          vanthalum antha condition remove panirum
        '''
        # isDirected=False itha yen potom yendral dircted ah iruntha ore dirction la tha flow aahum
        # apdi True nu kudutha example ku A directed to B , ithula A vanthu Buku direct conection irukum
        # B la iruntu A ku conection pogathu
        # inga False na undirected graph work aagum, True na dircted graph work aagum
        # directed Graph, A= {A:[b]}
        # but             B= {B:[]}
        # undirected Graph, A= {A:[b]}
        # but               B= {B:[A]}
        
        self.addvertex(vertex1)
        self.addvertex(vertex2)
        self.graph[vertex1].append(vertex2) # A to B ku
        # inga yena panrom na graph formal la irukuka vertax1 la irukka list la vertex 2 ah podrom
        if not isDirected:
            self.graph[vertex2].append(vertex1) #  to A realtion create aagum

vj=GRAPH()
#vj.addvertex('A')
#vj.addvertex('B') intha rendu step opda thevai ila ,because add edges la um vetrex ah add panirukon
vj.addedges("A","B")
vj.addedges("B","C")
vj.addedges("B","D")
vj.addedges("C","D")


