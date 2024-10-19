package coda.interfaccia;

public interface Coda {
    public void inserisci(int val);
    public int preleva();
    public boolean full();
    public boolean empty();
    public int getSize();
}
