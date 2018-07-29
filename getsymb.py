if __name__ == "__main__":
    import sys
    import argparse
    import finlib.core as finlib
    import pdb
    # python getsymb.py TWTR 1m 1week -fformat :6.2f -iformat :10d
    parser = argparse.ArgumentParser(description="Fetch price data for symbol.")
    parser.add_argument("symbol", help="The symbol to fetch data for.", type=str)
    parser.add_argument("interval", help="The sampling interval, e.g. '1d'.", type=str)
    parser.add_argument("time_string", help="The duration of interest as a time string, e.g. '1week'.", type=str)
    parser.add_argument("-fformat", help="Format string for integer information (e.g volume).", action="store", dest = "fformat", type=str)
    parser.add_argument("-iformat", help="Format string for float information (e.g. prices).",  action="store", dest = "iformat", type=str)    
    args = parser.parse_args()
    
    iformat = "{FMT}".replace("FMT", args.iformat if args.iformat else "")
    fformat = "{FMT}".replace("FMT", args.fformat if args.fformat else "")
    
    success, data = finlib.get_yahoo_quote(args.symbol, args.interval, args.time_string)
    if not success:
        print "Could not fetch data: {}".format(data["error"])
        exit(1)
    else:
        fields = ["t", "open", "close", "high", "low", "volume"]
        for i,t in enumerate(data["t"]):
            s = []
            for d in [data[f][i] for f in fields]:
                s.append(iformat.format(d) if type(d) is int else fformat.format(d) if type(d) is float else str(d))
            if i == 0:
                # Now that we know roughly how wide each field is going to be, print the header row positioned accordingly
                print "\t".join([fld[:len(s[ifld])] + " "*(len(s[ifld])- len(fld)) for ifld,fld in enumerate(fields)])
            print "\t".join(s)
        exit(0)
    
    
    


    
    
    
