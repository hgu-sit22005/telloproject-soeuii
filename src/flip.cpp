#include "flip.h"
#include <cstring>
#include <sstream>

Flip::Flip()
{
	command = new char[strlen("flip ")+1];
	strcpy(command, "flip ");
}



Flip::Flip(int _value)
{

	std::stringstream sstream;


	switch(_value)
	{
		case 0:
		sstream << "flip l";
		break;
		case 1:
		sstream << "flip r";
		break;
		case 2:
		sstream << "flip f";
		break;
		default:
		sstream << "flip b";
		break;
	}



	sstream << "flip " << _value;

	command = new char[strlen(sstream.str().c_str())+1];
	strcpy(command, sstream.str().c_str());
}


double Flip::get_delay()
{ 
	return 5; 
}