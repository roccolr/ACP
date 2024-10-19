package coda.implementazioni;

import coda.interfaccia.*;

public class CodaCircolare implements Coda{
    private int [] data;
    private int head;
    private int tail;
    private int elem;
    private int size;

    public CodaCircolare(int size){
        this.size = size;
        head = tail = 0;
        elem = 0;
        data = new int[size];
    }
    

    public boolean full(){
        if(elem == size){
            return true;
        }
        return false;
    }

    public boolean empty(){
        if(elem == 0){
            return true;
        }
        return false;
    }

    public int getSize(){
        return this.size;
    }

    public void inserisci(int val){
        data[head] = val;
        head = (head+1)%size;
        elem = elem + 1;
    }

    public int preleva(){
        int res = data[tail];
        tail = (tail+1)%size;
        elem = elem-1;
        return res;
    }
}
