package coda;

public abstract class CodaWrapper implements Coda {
    protected Coda coda;

    public CodaWrapper(Coda coda){
        this.coda = coda;
    }

    public boolean full(){
        return coda.full();
    }

    public boolean empty(){
        return coda.empty();
    }

    public int getSize(){
        return coda.getSize();
    }
}

//coda wrapper è una classe astratta, in modo che vengano forzate le implementazioni
// dei metodi preleva e inserisci. Questo per dividere la logica di gestione della coda
//dalla logica di sincronizzazione
