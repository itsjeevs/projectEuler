#!/Users/jejoseph/anaconda3/bin/python
import logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


def bracket_sanity_checker(input_string):
    bracket_list =  []
    bracket_map ={"[":"]","{":"}","(":")"}
    for i in input_string:
        logger.info(i+ "\t\tCurrent list: "+ "-".join(bracket_list))
        if i in bracket_map:
            bracket_list.append(i)
            logger.info("input: "+i+" push: "+ i)
        elif bracket_map[bracket_list[-1]] == i:
            logger.info("input: "+i+" pop: "+bracket_list[-1])
            bracket_list.pop()    
    return  len(bracket_list) == 0


# input_string = "{}({{[{}]}})[]"
input_string = "{ [ ( ] ) }"
print(bracket_sanity_checker(input_string))


