package interfacce;

public abstract class CodaWrapper implements Coda{
    // classe di utilità, il cui scopo è quello di implementare la sincornizzazione
    //gli altri metodi sono gestiti da Coda o sottotipi (codaCircolare)
    protected Coda coda;

    public CodaWrapper(Coda coda){
        this.coda = coda;
    }

    public boolean full(){
        System.out.println("testando la pienezza");
        return coda.full();
    }
    public boolean empty(){
        return coda.empty();
    }
    public int getSize(){
        return coda.getSize();
    }

}
